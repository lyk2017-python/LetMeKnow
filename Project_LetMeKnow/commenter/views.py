
from django.core.mail import send_mail
from django.shortcuts import render
from django.views import generic
from commenter.models import *


# Create your views here.
from commenter.templates.forms import ContactForm


class HomePageSummaryView(generic.ListView):
    model = Comment

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['summary'] = Comment.objects.filter


class HomePageView(generic.ListView):
    def get_queryset(self):
        return Comment.objects.all()


class CommentView(generic.DetailView):
    def get_queryset(self):
        return Comment.objects.all()


class SSSView(generic.TemplateView):
    template_name = "commenter/sss.html"


class ContactFormView(generic.FormView):
    form_class = ContactForm
    template_name = "commenter/contact.html"
    success_url = "/"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if(self.request.method in ["POST","PUT"]):
            post_data = kwargs["data"].copy()
            post_data["ip"] = self.request.META["REMOTE_ADDR"]
            kwargs["data"] = post_data
        return kwargs


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
         "ip={}").format(data["message"], data["email"], data["ip"]),
         settings.DEFAULT_FROM_EMAIL,
        ["tanerdurkut@gmail.com"]
        )
        return super().form_valid(form)

