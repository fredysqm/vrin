from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
admin.autodiscover()

urlpatterns = patterns('app.views',
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home_url'),
    url(r'^inscripcion/$', 'inscripcion_view', name='inscripcion_url'),
    url(r'^constancia/$', 'constancia_view', name='constancia_url'),
    url(r'^constancia/(\d+)/$', 'constancia_print_view', name='constancia_print_url'),
    url(r'^admin/', include(admin.site.urls)),
)