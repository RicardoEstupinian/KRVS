from django.conf.urls import include, url
from apps.log.views import vistalogin
urlpatterns = [
    url(r'^$', vistalogin,name='login'),
]
