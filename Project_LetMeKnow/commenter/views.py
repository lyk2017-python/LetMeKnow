from django.shortcuts import render
from django.views import generic
from commenter.models import *

# Create your views here.
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