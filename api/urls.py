from django.conf.urls import patterns, include, url

from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'participante', participante_view_set)
router.register(r'universidad', universidad_view_set)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    #url(r'^assdasd/$', 'existe_dni_view', name='existe_dni_url'),
    # url(r'^asistencia/(\d+)/(\d+)/$', 'asistencia_registro_view', name='asistencia_registro_url'),
)