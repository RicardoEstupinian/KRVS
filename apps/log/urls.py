from django.conf.urls import include, url
from apps.log.views import login
urlpatterns = [
    url(r'^$', login,name='login'),
]
