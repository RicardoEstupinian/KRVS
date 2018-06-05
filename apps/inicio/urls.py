from django.conf.urls import include, url
from apps.inicio.views import inicio
urlpatterns = [
    url(r'^inicio/', inicio),
]
