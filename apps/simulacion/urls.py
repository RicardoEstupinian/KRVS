from django.conf.urls import include, url
from apps.simulacion.views import simular
urlpatterns = [
    url(r'^$', simular),
]
