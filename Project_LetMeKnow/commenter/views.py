from django.shortcuts import render
from django.views import generic
from commenter.models import *

# Create your views here.
class HomePageView(generic.ListView):
    def get_queryset(self):
        return Comment.objects.all()

class DetailView(generic.DetailView):
    def get_queryset(self):
        return Comment.objects.filter()

class SSSView(generic.TemplateView):
    template_name = "commenter/sss.html"