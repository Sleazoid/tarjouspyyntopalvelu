from django.conf.urls import patterns, include, url

urlpatterns = patterns('tarjoukset.views',
    url(r'^$', 'index'),
    url(r'^contacte/$', 'contacte'),
    url(r'^selaa/$', 'selaa'),
 
)

