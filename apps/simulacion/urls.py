from django.conf.urls import include, url
from apps.simulacion.views import simulador_view
urlpatterns = [
    url(r'^$', simulador_view),
]
