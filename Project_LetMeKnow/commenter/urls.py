from django.conf.urls import url
from commenter.views import HomePageView, CommentView, SSSView


urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^detail/(?P<pk>\d+)$', CommentView.as_view(), name='commentdetails'),
    url(r'^sss$', SSSView.as_view(), name="faq")
]

