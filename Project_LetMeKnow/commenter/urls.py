from django.conf.urls import url
from commenter.views import HomePageView, DetailView, SSSView


urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^detail/(?P<id>\d+)$', DetailView.as_view(), name='commentdetails'),
    url(r'^sss$', SSSView.as_view(), name="faq")
]

