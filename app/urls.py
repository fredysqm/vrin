from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from .views import participante_crear_view, participante_crear_final_view, participante_constancia_view, participante_constancia_print_view

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home_url'),
    url(r'^inscripcion/$', participante_crear_view.as_view(), name='participante_crear_url'),
    url(r'^inscripcion/(?P<pk>\d+)/$', participante_crear_final_view.as_view(), name='participante_crear_final_url'),
    url(r'^constancia/$', participante_constancia_view.as_view(), name='participante_constancia_url'),
    url(r'^constancia/(?P<pk>\d+)/$', participante_constancia_print_view.as_view(), name='participante_constancia_print_url'),
    # url(r'^asistencia/$', 'asistencia_view', name='asistencia_url'),
    # url(r'^asistencia/(\d+)/(\d+)/$', 'asistencia_registro_view', name='asistencia_registro_url'),
)