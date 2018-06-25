from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login,logout_then_login

urlpatterns = [
    # Examples:
    # url(r'^$', 'KRVS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^simulacion/', include('apps.simulacion.urls',namespace="simulacion")),
    url(r'^inicio/', include('apps.inicio.urls',namespace="inicio")),
    url(r'^modificacion/', include('apps.solicitud.urls',namespace="modificacion")),
    url(r'^informacion/', include('apps.inicio.urls',namespace="informacion")),
    url(r'^accounts/login', login,{'template_name':'login/login_index.html'},name='login'),
    url(r'^logout/',logout_then_login,name='logout'),
]
