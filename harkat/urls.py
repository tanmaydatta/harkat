from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # Examples:
    # url(r'^$', 'harkat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/', include('api.urls')),
]
