from django.conf.urls import include, url
from apps.inicio.views import inicio,infor

from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', login_required(inicio),name='inicio'),
    url(r'^infor$', login_required(infor),name='informacion'),
]
