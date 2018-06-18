from django.conf.urls import include, url
from apps.inicio.views import inicio,infor
urlpatterns = [
    url(r'^$', inicio,name='inicio'),
    url(r'^infor$', infor,name='informacion'),
]
