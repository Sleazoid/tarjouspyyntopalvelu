from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from accounts.forms import SignupFormExtra
from accounts.models import TarjousModelFormPreview
from tarjoukset.models import TarjousModelForm
from django import forms
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rose.views.home', name='home'),
    # url(r'^rose/', include('rose.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^asiakastarjoukset/', include('asiakastarjoukset.urls')),
    url(r'^tarjoukset/', include('tarjoukset.urls')),
  #  (r'^accounts/', include('rekisterointi.urls')),
    url(r'^postman/',include('postman.urls')),
    (r'^forms/', include('form_designer.urls')),
    (r'^contact/', include('contact_form.urls')),
    #(r'^contacts/', 'contacts.views.main'),
 #   (r'^accounts/None/signup/complete
    (r'^accounts/signup/$',
     'accounts.views.signup',
     {'signup_form': SignupFormExtra}),
 
    (r'^post/$', TarjousModelFormPreview(TarjousModelForm)),
    (r'^tyopaikat/', include('tyopaikat.urls')),
    (r'^accounts/', include('accounts.urls')),
    url(r'^toimialakategoriat/', include('toimialakategoriat.urls')),
    
      # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
  
     url(r'^', include('cms.urls')),
#	(r'','rainbow.views.index'),
)
if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns
