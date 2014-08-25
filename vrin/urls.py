from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('app.views',
    url(r'^inscripcion/$', 'inscripcion_view', name='inscripcion_url'),
    url(r'^admin/', include(admin.site.urls)),
)
