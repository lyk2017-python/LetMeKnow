from functools import reduce

from django.contrib.postgres.search import SearchVector
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
import operator
from django.db.models import Q



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


class HomePageView(generic.ListView):
    """This class lists latest comments and most commented products"""
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

class ProductCommentList(generic.ListView):
    """This class lists  all comments for a given product"""
    template_name = 'commenter/product_comment_list.html'
    context_object_name = 'product'
    model = Comment

    def get_queryset(self):
        qs = super(ProductCommentList, self).get_queryset()
        return qs.filter(product_id = self.kwargs['pk'])

class SSSView(generic.TemplateView):
    template_name = "commenter/sss.html"


class CommentDetailView(generic.DetailView):
    """This class gives all details of a singe comment"""
    model = Comment


class CommentView(LoginCreateView):
    """This class creates new comment"""
    form_class = CommentForm
    template_name = "commenter/comment_create.html"
    success_url = "./success/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(LoginCreateView, self).form_valid(form)

class ProductView(generic.CreateView):
    """This clas creates ne product"""
    form_class = ProductForm
    template_name = "commenter/product_create.html"
    success_url = "./success"


class ContactFormView(generic.FormView):
    """This class creates contact message and writes it to disk"""
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


def signup_success(request):
    return render(request, 'commenter/signup_success.html')


class RegistrationView(generic.FormView):
    """This class enables user signup"""
    form_class = CustomUserCreationForm
    template_name = "commenter/signup.html"
    success_url = "./success/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class SearchView(HomePageView):
    """This class lets user search in database restricted just three columns comment title, content and product name"""
    template_name = 'commenter/search_list.html'
    context_object_name = 'search_object'
    model = Comment, Product


    def get_queryset(self):
        qs = super(SearchView, self).get_queryset()
        query = self.request.GET.get('keyword', "")
        #return qs.filter(product__name__icontains=query)
        return qs.filter(Q(product__name__icontains=query) | Q(title__icontains=query) | Q(message__icontains=query))

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        query = self.request.GET.get('keyword', "")
        context.update(
                {
                    'search_keyword':query,

                }
            )
        return context