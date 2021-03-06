# -*- coding: utf-8 -*-

from django.template import Context, loader
from tarjoukset.models import Choice, Poll, TarjousModel, TarjousModelForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.template import RequestContext, Context
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
import datetime
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django import forms
from django.forms.widgets import *
from toimialakategoriat.models import Toimiala
from django.core.mail import send_mail, BadHeaderError, send_mass_mail
from accounts.models import MyProfile
class ContactView(FormView):
    template_name = 'contact.html'
    form_class = TarjousModelForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_mail(
cd['subject'],
cd['message'],
cd.get('email', 'noreply@example.com'),
['tapio.tomi@gmail.com'],
) 
        return super(ContactView, self).form_valid(form)

def index(request):
    if request.method == 'POST': # If the form has been submitted...
        form = TarjousModelForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
	    instance = form.save()
	    instance.save()	    		            
		# Process the data in form.cleaned_data
            # ...  
	    subject = form.cleaned_data['otsikko']
	    message = ''
	    message = message + u'Tarjouspyynnon lähettäjän nimi: '+'%s %s' %(form.cleaned_data ['etunimi'], form.cleaned_data['sukunimi'])
	    message = message +"\n"+ u'Sähköpostiosoite: '+'%s' %(form.cleaned_data['email'])
	    message = message +"\n"+ u'Puhelinnumero: '+'%s' %(form.cleaned_data['puhelinnumero'])
   	    message = message +"\n"+ u'Toimiala: '+'%s' %(form.cleaned_data['toimiala'])
	    message = message +"\n"+ u'Tarjoukset viimeistään: '+'%s' %(form.cleaned_data['tarjoukset_viimeistaan'])
	    message = message +"\n"+ u'Haetaan alueelta: '+'%s' %(form.cleaned_data['alue'])
	    message = message +"\n\n"+ '%s' %(form.cleaned_data['tarjouspyynto'])
	    
	    #name = form.cleaned_data['name']
       	    toimiala_osoitettu = form.cleaned_data['toimiala']
           #message = form.cleaned_data['comment']
            sender = 'tapio.tomi@gmail.com'
	    receiver = ['tapio.tomi@gmail.com']
	    kayttaja =''
	   # for a in MyProfile.objects.all():
		#if (a.toimiala==toimiala_osoitettu):
		#	kayttaja=(a.user)
		#	sposti=User.objects.filter(username__exact=kayttaja).values_list('email', flat=True)
		#	send_mail(subject, message, sender, sposti)
	    send_mail(subject, message,sender,receiver)
	  ##  user = MyProfile.objects.filter(toimiala__exact=toimiala_osoitettu)
	#    username = User.objects.filter(username__exact=user)
	   ## sposti=User.objects.filter(username__exact=user).values_list('email', flat=True)

	   #for user in User.objects.all():
		#if User.objects.filter(
            #user = User.objects.get(email='tapio.tomi@edu.ramk.fi')
	    #recipients = [User.objects.get(email='tapio.tomi@gmail.com')]
	   # if (User.MyProfile.toimiala = toimiala_osoitettu)
	   ## recipients = ['tapio.tomi@gmail.com','tomi@nettitaivas.com']
          ##  recipients2 = sposti
            #if cc_myself:
             #  recipients.append(sender)
	#    send_mail(subject, message, sender, recipients)
	#    send_mail('Subject here', 'Here is the message.', 'tapio.tomi@gmail.com',
    	 #   ['tomi.tapio@edu.ramk.fi','tapio.tomi@gmail.com'], fail_silently=False)
	   # sender = form.cleaned_data['sender']
	    #cc_myself = form.cleaned_data['cc_myself']
	    #recipients = ['tapio.tomi@gmail.com']
	    #if cc_myself:
	#	recipients.append(sender)
	 #   from django.core.mail import send_mail
	##    send_mail(subject, message, sender, recipients2)
            return HttpResponseRedirect('/tarjoukset/contacte/') # Redirect after POST
	    #return redirect(contact)
    else:
        form = TarjousModelForm() # An unbound form

    return render(request, 'tarjoukset/index.html', {
        'form': form
    })

def contacte(request):


    return render_to_response('tarjoukset/detail.html',
                               context_instance=RequestContext(request))

def selaa(request):

   #   html ="<html><body>It is now %s.</body></html>" %now
  #    return HttpResponse(html)
    # for d in Toimiala.objects.all():
     #toimi_=Toimiala.objects.filter(toimiala__exact='Siivous')
      html = []
     
      for t in TarjousModel.objects.all():
	counter =t
	if t.tarjoukset_viimeistaan < datetime.date.today(): 
#	html ="<html><body> %s.</body></html>" %t.tarjouspyynto
		juu = t.tarjouspyynto
		jaa = t.otsikko	
		html.append(dict(juu=juu,jaa=jaa))
	
  #    return HttpResponse(html)	
	#form = t.tarjouspyynto
#TarjousModel.objects.filter(toimiala=toimi_)
      return render_to_response('tarjoukset/selaa.html',
	{'form': html,},
	context_instance=RequestContext(request))
    # If no usernames are wanted and the default form is used, fallback to the
    # default form that doesn't display to enter the username.
   #  p = get_object_or_404(Poll, pk=tarjousmodel_id)

#     return render(request, 'profile_detail.html', {
 #       'form': form
  #  })
    # return render_to_response('profile_detail.html', {'form': p},
     #                          context_instance=RequestContext(request))
     
def detail(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('tarjoukset/detail.html', {'poll': p},
                               context_instance=RequestContext(request))

def results(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('tarjoukset/results.html', {'poll': p})
def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('tarjoukset/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('tarjoukset.views.results', args=(p.id,)))
