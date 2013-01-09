# -*- coding: utf-8 -*-
from tarjoukset.models import TarjousModel,TarjousModelForm
from django.core.mail import send_mail
#from forms import CommentForm
from django.contrib import admin
#from formadmin import sites
from django.contrib.auth.models import User
from accounts.models import MyProfile
class TarjousModelAdmin(admin.ModelAdmin):
    actions = ['send_mail','julkaise']
    fields = ('etunimi', 'sukunimi', 'email', 'puhelinnumero', 'toimiala', 'tarjoukset_viimeistaan','alue','otsikko','tarjouspyynto')
    form = TarjousModelForm
    list_display = ['otsikko', 'toimiala','etunimi','sukunimi','is_public','mailed','tarjoukset_viimeistaan']
   
	    #name = form.cleaned_data['name']
    toimiala_osoitettu = 'toimiala'
           #message = form.cleaned_data['comment']
    sender = 'tapio.tomi@gmail.com'
    kayttaja =''
    def julkaise(ModelAdmin, request, queryset):
   	 queryset.update(is_public=True)
	 ModelAdmin.message_user(request, "Valitut tarjouspyynnöt ovat asetettu julkisiksi.")
    def send_mail(self, request, queryset):
     if request.method == 'POST': # If the form has been submitted...
     
      for objects in queryset:
	subject = objects.otsikko
	message = ''
  	message = message + u'Tarjouspyynnon lähettäjän nimi: '+'%s %s' %(objects.etunimi, objects.sukunimi)
  	message = message +"\n"+ u'Sähköpostiosoite: '+'%s' %(objects.email)
  	message = message +"\n"+ u'Puhelinnumero: '+'%s' %(objects.puhelinnumero)
  	message = message +"\n"+ u'Toimiala: '+'%s' %(objects.toimiala)
  	message = message +"\n"+ u'Tarjoukset viimeistään: '+'%s' %(objects.tarjoukset_viimeistaan)
  	message = message +"\n"+ u'Haetaan alueelta: '+'%s' %(objects.alue)
  	message = message +"\n\n"+ '%s' %(objects.tarjouspyynto)
	toimiala_osoitettu=objects.toimiala
    	for a in MyProfile.objects.all():
	
  	 
  	  
	  if (a.toimiala==toimiala_osoitettu):
			kayttaja=(a.user)
			sposti=User.objects.filter(username__exact=kayttaja).values_list('email', flat=True)
			send_mail(subject, message, 'tapio.tomi@gmail.com', sposti)
      self.message_user(request, "Valitut tarjouspyynnöt lähettetty toimialoja vastaaville yrityksille.")
      queryset.update(mailed=True)
    send_mail.short_description = "send email"
    send_mail.allow_tags = True
    julkaise.short_description = "julkaise"
    julkaise.allow_tags = True
#class CommentFormAdmin(admin.ModelForm):
#	nimi = 'nimi'
#	email = 'email'
#sites.register(CommentForm, CommentFormAdmin)

admin.site.register(TarjousModel,TarjousModelAdmin)

