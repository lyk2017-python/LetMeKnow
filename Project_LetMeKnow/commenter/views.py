
from django.shortcuts import render
from django.http import Http404
from django.views import generic
from commenter.forms import CommentForm, ContactForm
from commenter.models import *
from django.core.mail import send_mail



# Create your views here.
class HomePageSummaryView(generic.ListView):
    model = Comment

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['summary'] = Comment.objects.filter

class HomePageView(generic.ListView):
    def get_queryset(self):
        return Comment.objects.all()



class SSSView(generic.TemplateView):
    template_name = "commenter/sss.html"


class CommentView(generic.CreateView):
    form_class = CommentForm
    template_name = "commenter/comment_create.html"
    success_url = "."

    def get_comment(self):
        query = Comment.objects.filter(slug=self.kwargs["slug"])
        if query.exists():
            return query.get()
        else:
            raise Http404("Category not found")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.method in ["POST", "PUT"]:
            post_data = kwargs["data"].copy()
            post_data["Comment"] = [self.get_comment()]
            kwargs["data"] = post_data
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = self.get_comment()
        return context




class ContactFormView(generic.FormView):
    form_class = ContactForm
    template_name = "blog/contact.html"
    success_url = "/"

    def form_valid(self, form):
        data = form.cleaned_data
        from django.conf import settings
        send_mail(
            "YilanTerbiyecisi ContactForm : {}".format(data["title"]),
            ("Sistemden size gelen bir bildirim var\n"
             "---\n"
             "{}\n"
             "---\n"
             "eposta={}\n"
             "ip={}").format(data["body"], data["email"], self.request.META["REMOTE_ADDR"]),
            settings.DEFAULT_FROM_EMAIL,
            ["cediddi@yilanterbiyecisi.com"]
        )
        return super().form_valid(form)
