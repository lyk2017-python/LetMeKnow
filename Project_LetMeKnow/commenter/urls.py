from django.conf.urls import url
from commenter.views import HomePageView, CommentDetailView, SSSView, ContactFormView, CommentView, ProductView, \
    comment_success, product_success

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^detail/(?P<pk>\d+)$', CommentDetailView.as_view(), name='commentdetails'),
    url(r'^sss$', SSSView.as_view(), name="faq"),
    url(r'^contact/$', ContactFormView.as_view(), name="contactform"),
    url(r'^comment/$', CommentView.as_view(), name="commentform"),
    url(r'^product/$', ProductView.as_view(), name="productform"),
    url(r'^comment/success/$', comment_success),
    url(r'^product/success/$', product_success),

]

