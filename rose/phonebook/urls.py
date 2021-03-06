from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('phonebook.views',
    url(r'^$', 'contacts'),
    url(r'^contacts/$', 'contacts'),  
    url(r'^contact_add/$', 'contact_add'),
    url(r'^contact_edit/(?P<contact_id>\d+)/$',
		'contact_edit'),
    url(r'^contact_delete/(?P<contact_id>\d+)/$',
		'contact_delete'),
)
