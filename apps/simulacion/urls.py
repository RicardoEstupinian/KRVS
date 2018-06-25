from django.conf.urls import include, url
from apps.simulacion.views import simulador_view
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$',login_required(simulador_view),name='simulacion'),
]
