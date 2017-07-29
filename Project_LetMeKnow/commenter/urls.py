from django.conf.urls import url
from commenter.views import HomePageView, CommentDetailView, SSSView, ContactFormView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^detail/(?P<pk>\d+)$', CommentDetailView.as_view(), name='commentdetails'),
    url(r'^sss$', SSSView.as_view(), name="faq"),
    url(r'^contact/$', ContactFormView.as_view(), name="contactform")
]

