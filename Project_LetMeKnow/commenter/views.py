from django.core.mail import send_mail
from django.http import Http404, request, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from commenter.forms import ContactForm, CommentForm, ProductForm, CustomUserCreationForm
from commenter.models import *
from django.db.models import F
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required



class LoginCreateView(LoginRequiredMixin, generic.CreateView):
    pass

def like(request):
    id = request.POST.get("id", default=None)
    like = request.POST.get("like")
    obj = get_object_or_404(Comment, id=int(id))
    if like == "true":
        obj.like = F("like") + 1
        obj.save(update_fields=["like"])

    else:
        return HttpResponse(status=400)
    obj.refresh_from_db()
    return JsonResponse({"like": obj.like, "id": id})

def dislike(request):
    id = request.POST.get("id", default=None)
    dislike = request.POST.get("dislike")
    obj = get_object_or_404(Comment, id=int(id))
    if dislike == "true":
        obj.dislike = F("dislike") + 1
        obj.save(update_fields=["dislike"])

    else:
        return HttpResponse(status=400)
    obj.refresh_from_db()
    return JsonResponse({"dislike": obj.dislike, "id": id})

"""This class lists latest comments and most commented products"""
class HomePageView(generic.ListView):
    template_name = 'commenter/comment_list.html'
    context_object_name = 'comment_series_list'
    model = Comment

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context.update(
            {
                'product_series_list':Product.objects.order_by('name'),

            }
        )
        return context

    def get_queryset(self):
        return Comment.objects.all()

"""This class lists  all comments for a given product"""
class ProductCommentList(generic.ListView):
    template_name = 'commenter/product_comment_list.html'
    context_object_name = 'product'
    model = Comment

    def get_queryset(self):
        qs = super(ProductCommentList, self).get_queryset()
        return qs.filter(product_id = self.kwargs['pk'])



class SSSView(generic.TemplateView):
    template_name = "commenter/sss.html"

"""This class gives all details of a singe comment"""
class CommentDetailView(generic.DetailView):
    model = Comment

"""This class creates new comment"""
class CommentView(LoginCreateView):
    form_class = CommentForm
    template_name = "commenter/comment_create.html"
    success_url = "./success/"

"""This clas creates ne product"""
class ProductView(generic.CreateView):
    form_class = ProductForm
    template_name = "commenter/product_create.html"
    success_url = "./success"

"""This class creates contact message and writes it to disk"""
class ContactFormView(generic.FormView):
    form_class = ContactForm
    template_name = "commenter/contact.html"
    success_url = "/"

    def form_valid(self, form):
        data = form.cleaned_data
        from django.conf import settings
        send_mail(
        "LetMeKnow ContactForm : {}".format(data["subject"]),
        ("You have a message\n"
         "---\n"
         "{}\n"
         "---\n"
         "email={}\n"
         "ip={}").format(data["message"], data["email"], self.request.META["REMOTE_ADDR"]),
         settings.DEFAULT_FROM_EMAIL,
         ["tanerdurkut@gmail.com"]
        )
        return super().form_valid(form)


def comment_success(request):
    return render(request, 'commenter/comment_success.html')


def product_success(request):
    return render(request, 'commenter/product_success.html')

class RegistrationView(generic.FormView):
    form_class = CustomUserCreationForm
    template_name = "commenter/signup.html"
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)




class SearchView(HomePageView):
    paginate_by = 10

    def get_queryset(self):
        result = super(HomePageView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:

            result = result.filter(name__icontains=query)

        return result
