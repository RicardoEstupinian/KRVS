from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'KRVS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^simulacion/', include('apps.simulacion.urls',namespace="simulacion")),
    url(r'^inicio/', include('apps.inicio.urls',namespace="inicio")),
    url(r'^modificacion/', include('apps.solicitud.urls',namespace="modificacion")),
]
