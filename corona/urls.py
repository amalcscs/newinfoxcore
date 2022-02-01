from django.contrib import admin
from django.urls import re_path, include

from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    re_path(r'^admin$', admin.site.urls),
    re_path(r'^$', views.ini, name='ini'),
    re_path(r'^corapp/', include('corapp.urls')),
]
