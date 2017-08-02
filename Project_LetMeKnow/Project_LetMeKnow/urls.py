from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views import static
from django.contrib.auth import views as auth_views
from commenter.urls import urlpatterns as commenter_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(commenter_urls)),
    url(r'^accounts/login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
]

if settings.DEBUG:
    urlpatterns.append(
        url(r"^media/(?P<path>.*)$", static.serve, {'document_root': settings.MEDIA_ROOT})
    )
