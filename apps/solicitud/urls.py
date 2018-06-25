from django.conf.urls import include, url
from apps.solicitud.views import modificacion 
from django.contrib.auth.decorators import login_required
urlpatterns = [
    url(r'^$', login_required(modificacion),name='modificacion'),
]