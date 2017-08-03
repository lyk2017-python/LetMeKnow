from django.conf.urls import url
from commenter.views import HomePageView, CommentDetailView, SSSView, ContactFormView, CommentView, ProductView, \
    comment_success, product_success, ProductCommentList, like, dislike, RegistrationView, signup_success,SearchView

appname = 'commenter'

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^detail/(?P<pk>\d+)$', CommentDetailView.as_view(), name='commentdetails'),
    url(r'^sss$', SSSView.as_view(), name="faq"),
    url(r'^contact/$', ContactFormView.as_view(), name="contactform"),
    url(r'^comment/$', CommentView.as_view(), name="commentform"),
    url(r'^product/$', ProductView.as_view(), name="productform"),
    url(r'^comment/success/$', comment_success),
    url(r'^product/success/$', product_success),
    url(r'^signup/success/$', signup_success),

    url(r'^product/(?P<pk>\d+)$', ProductCommentList.as_view(), name='product_comment_list'),
    url(r"^api/like$", like, name="like_dislike"),
    url(r"^api/dislike$", dislike, name="dislike"),
    url(r"^signup/$", RegistrationView.as_view(), name="register"),
    url(r'^search/$', SearchView.as_view(), name='list-search'),
]

