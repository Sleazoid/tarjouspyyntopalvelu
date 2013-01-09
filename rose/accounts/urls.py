from django.conf.urls.defaults import *
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from accounts import views as userena_views
from accounts import settings as userena_settings

urlpatterns = patterns('',
    # Signup, signin and signout
    url(r'^signup/$',
       userena_views.signup,
       name='userena_signup'),
    url(r'^signin/$',
       userena_views.signin,
       name='userena_signin'),
    url(r'^signout/$',
       userena_views.signout,
       name='userena_signout'),

    # Reset password
    url(r'^password/reset/$',
       auth_views.password_reset,
       {'template_name': 'userena/password_reset_form.html',
        'email_template_name': 'userena/emails/password_reset_message.txt'},
       name='userena_password_reset'),
    url(r'^password/reset/done/$',
       auth_views.password_reset_done,
       {'template_name': 'userena/password_reset_done.html'},
       name='userena_password_reset_done'),
    url(r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
       auth_views.password_reset_confirm,
       {'template_name': 'userena/password_reset_confirm_form.html'},
       name='userena_password_reset_confirm'),
    url(r'^password/reset/confirm/complete/$',
       auth_views.password_reset_complete,
       {'template_name': 'userena/password_reset_complete.html'}),

   

    # Activate
    url(r'^activate/(?P<activation_key>\w+)/$',
       userena_views.activate,
       name='userena_activate'),

    # Change email and confirm it
    url(r'^(?P<username>[\.\w]+)/email/$',
       userena_views.email_change,
       name='userena_email_change'),
    url(r'^(?P<username>[\.\w]+)/email/complete/$',
       userena_views.direct_to_user_template,
       {'template_name': 'userena/email_change_complete.html'},
       name='userena_email_change_complete'),
    url(r'^(?P<username>[\.\w]+)/confirm-email/complete/$',
       userena_views.direct_to_user_template,
       {'template_name': 'userena/email_confirm_complete.html'},
       name='userena_email_confirm_complete'),
    url(r'^confirm-email/(?P<confirmation_key>\w+)/$',
       userena_views.email_confirm,
       name='userena_email_confirm'),

    # Disabled account
    url(r'^(?P<username>[\.\w]+)/disabled/$',
       userena_views.direct_to_user_template,
       {'template_name': 'userena/disabled.html'},
       name='userena_disabled'),

    # Change password
    url(r'^(?P<username>[\.\w]+)/password/$',
       userena_views.password_change,
       name='userena_password_change'),
    url(r'^(?P<username>[\.\w]+)/password/complete/$',
       userena_views.direct_to_user_template,
       {'template_name': 'userena/password_complete.html'},
       name='userena_password_change_complete'),

    # Edit profile
    url(r'^(?P<username>[\.\w]+)/edit/$',
       userena_views.profile_edit,
       name='userena_profile_edit'),
    # pyynnot profile
    url(r'^(?P<username>[\.\w]+)/pyynnot/$',
       userena_views.profile_pyynnot,
       name='userena_profile_pyynnot'),
    url(r'^(?P<username>[\.\w]+)/tyopaikat/$',
       userena_views.tyopaikat,
       name='userena_tyopaikat'),
    url(r'^(?P<username>[\.\w]+)/tyopaikat/complete/$',
       userena_views.direct_to_user_template,
       {'template_name': 'userena/tyopaikka_complete.html'},
       name='userena_tyopaikat_complete'),
    url(r'^(?P<username>[\.\w]+)/tyopaikat/details/$',
       userena_views.tyopaikat_detail,
       {'template_name': 'userena/tyopaikka_detail.html'},
       name='userena_tyopaikat_detail'),
    url(r'^(?P<username>[\.\w]+)/tyopaikat/delete/(?P<id>[\.\w]+)/$',
       userena_views.delete_tp,
#       {'template_name': 'userena/delete_tp.html'},
       
       name='userena_delete_tp'),
    url(r'^(?P<username>[\.\w]+)/tyopaikat/deletecomplete/$',  
	userena_views.direct_to_user_template,
	{'template_name': 'userena/delete_tp.html'},
	name='userena_deletecomplete'),
  
 # Signup
    url(r'^(?P<username>[\.\w]+)/signup/complete/$',
       userena_views.direct_to_user_template,
       {'template_name': 'userena/signup_complete.html',
        'extra_context': {'userena_activation_required': userena_settings.USERENA_ACTIVATION_REQUIRED,
                          'userena_activation_days': userena_settings.USERENA_ACTIVATION_DAYS}},
       name='userena_signup_complete'),
    # View profiles
    url(r'^(?P<username>(?!signout|signup|signin)[\.\w]+)/$',
       userena_views.profile_detail,
       name='userena_profile_detail'),
    url(r'^page/(?P<page>[0-9]+)/$',
       userena_views.ProfileListView.as_view(),
       name='userena_profile_list_paginated'),
    url(r'^$',
       userena_views.ProfileListView.as_view(),
       name='userena_profile_list'),
)
