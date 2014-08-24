from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('app.views',
    url(r'^$', 'home_view', name='home_url'),
    url(r'^admin/', include(admin.site.urls)),
)
