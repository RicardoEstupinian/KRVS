from django.conf.urls import include, url
from apps.solicitud.views import modificacion 
urlpatterns = [
    url(r'^$', modificacion),
]