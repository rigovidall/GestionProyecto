__author__ = 'rvidal'
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = patterns('',
    # Examples:
    url(r'^index/$', 'usuario.views.inicio', name='Inicio'),
    # url(r'^blog/', include('blog.urls')),

    #Usuarios
    url(r'^usuario/nuevo/$', 'usuario.views.nuevo_usuario', name='registrar_usuario'),
    url(r'^usuario/login/$', 'usuario.views.iniciar_sesion', name='iniciar_sesion'),
    url(r'^usuario/logout/$', 'usuario.views.cerrar_sesion', name='Cerrar Sesion'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^usuario/new/$', 'usuario.views.nuevo_user'),
    url(r'^usuario/lista/$', login_required(views.UsuarioList.as_view()), name='usuario_lista'),
    url(r'^modificar/(?P<pk>\d+)$', login_required(views.UpdateUser.as_view()), name='modificar_usuario'),
    url(r'^cambiar_clave/(?P<pk>\d+)$', login_required('usuario.views.cambio_clave'), name='cambio_clave'),

)
