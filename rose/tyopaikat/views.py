# -*- coding: utf-8 -*-
import datetime
from userena.decorators import secure_required
from django.shortcuts import render_to_response, redirect, get_object_or_404
from tarjoukset.models import Choice, Poll, TarjousModel, TarjousModelForm
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, REDIRECT_FIELD_NAME
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import logout as Signout
from django.views.generic import TemplateView
from django.template.context import RequestContext
from django.views.generic.list import ListView
from django.conf import settings
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.http import HttpResponseForbidden, Http404
from tyopaikat.models import TyopaikkaModel
from haku.models import HakuModel, HakuModelForm
from userena.forms import (SignupForm, SignupFormOnlyEmail, AuthenticationForm,
                           ChangeEmailForm, EditProfileForm)
from userena.models import UserenaSignup
from userena.decorators import secure_required
from userena.backends import UserenaAuthenticationBackend
from userena.utils import signin_redirect, get_profile_model
from userena import signals as userena_signals
from accounts import settings as userena_settings
from tyopaikat.models import TyopaikkaModelForm
from guardian.decorators import permission_required_or_403

import warnings
def tyopaikat_haku(request):
   if request.method == 'POST': # If the form has been submitted...
        form = HakuModelForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
	     toimiala = form.cleaned_data['toimiala']
	    
	     alue = form.cleaned_data[u'alue']
             redirect_to = reverse('tyopaikat_selaa', kwargs={'alue': alue,'toimiala':toimiala})
             return redirect(redirect_to)
	  #   return HttpResponseRedirect(reverse('/tyopaikat/tyopaikat_selaa/', kwargs={'alue':alue})) # Redirect after POST
	    #return redirect(contact)
   else:
        form = HakuModelForm() # An unbound form

   return render(request, 'userena/tyopaikat_haku.html', {
        'form': form
    })


def tyopaikat_selaa(request,alue,toimiala, **kwargs):
    toimialar=toimiala
    aluen=alue
    html = []
 
 #   for w in TyopaikkaModel.objects.filter(alue__iexact=aluen):
    for w in TyopaikkaModel.objects.filter(toimiala__toimiala=toimialar,alue__iexact=aluen):      
	if w.haku_viimeistaan > datetime.date.today():
	   # if (w.toimiala_id=1):	
	#    MyProfile.objects.filter(toimiala_id=Rakennus)

		yritys = w.yrityksen_nimi
		email = w.email
		etunimi = w.etunimi
		sukunimi = w.sukunimi
		toimiala = w.toimiala
		kaupunki = w.kaupunki
		haku_viimeistaan = w.haku_viimeistaan
		otsikko = w.otsikko
		kuvaus = w.kuvaus
		html.append(dict(yritys=yritys,email=email,etunimi=etunimi,sukunimi=sukunimi,toimiala=toimiala,alue=kaupunki,haku_viimeistaan=haku_viimeistaan,otsikko=otsikko,kuvaus=kuvaus))
    return render_to_response('userena/tyopaikat_selaa.html',
	{'form': html,},
	context_instance=RequestContext(request))
