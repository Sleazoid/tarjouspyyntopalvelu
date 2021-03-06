# -*- coding: utf-8 -*-
from django.db import models
import datetime
from django.utils import timezone
from django import forms
from toimialakategoriat.models import Toimiala 
from django.forms import ModelForm, Textarea
from django.forms.widgets import *
from django.core.mail import send_mail, BadHeaderError

MY_DATE_FORMATS = ['%d.%m.%Y',]

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
	return self.question
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()
    def __unicode__(self):
	return self.choice


class TarjousModel(models.Model):
    LAPPI = 'Lappi'
    AHVENANMAA = 'Ahvenanmaa'
    ETELAPOHJANMAA = u'Etelä-Pohjanmaa'
    ETELASAVO = u'Etelä-Savo'
    KAINUU = 'Kainuu'
    KANTAHAME = u'Kanta-Häme'
    KESKIPOHJANMAA ='Keskipohjanmaa'
    KESKISUOMI ='Keski-Suomi'
    KYMENLAAKSO ='Kymenlaakso'
    PIRKANMAA ='Pirkanmaa'
    POHJANMAA ='Pohjanmaa'
    POHJOISKARJALA ='Pohjois-Karjala'
    POHJOISPOHJANMAA ='Pohjois-Pohjanmaa'
    POHJOISSAVO ='Pohjois-Savo'
    PAIJATHAME =u'Päijät-Häme'
    SATAKUNTA = 'Satakunta'
    UUSIMAA ='Uusimaa'
    VARSINAISSUOMI ='Varsinais-Suomi'

    LAANIT_CHOICES =(
	
	(AHVENANMAA, 'Ahvenanmaa'),
	(ETELAPOHJANMAA, 'Etelä-pohjanmaa'),
	(ETELASAVO, 'Etelä-Savo'),
	(KAINUU, 'Kainuu'),
	(KANTAHAME, 'Kanta-Häme'),
	(KESKIPOHJANMAA, 'Keski-Pohjanmaa'),
	(KESKISUOMI, 'Keski-Suomi'),
	(KYMENLAAKSO, 'Kymenlaakso'),
        (LAPPI, 'Lappi'),
	(PIRKANMAA, 'Pirkanmaa'),
	(POHJANMAA, 'Pohjanmaa'),
	(POHJOISKARJALA, 'Pohjois-Karjala'),
	(POHJOISPOHJANMAA, 'Pohjois-Pohjanmaa'),
	(POHJOISSAVO, 'Pohjois-Savo'),
	(PAIJATHAME, 'Päijät-Häme'),
	(SATAKUNTA, 'Satakunta'),
	(UUSIMAA, 'Uusimaa'),
	(VARSINAISSUOMI, 'Varsinais-Suomi'),

    )
    etunimi = models.CharField(max_length=200 )
    sukunimi = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    puhelinnumero = models.CharField(max_length=200)
    
    toimiala = models.ForeignKey('toimialakategoriat.Toimiala')
    tarjoukset_viimeistaan = models.DateField()

    alue = models.CharField(max_length=15,
				choices=LAANIT_CHOICES,
				default=LAPPI)
    otsikko = models.CharField(max_length=200)
    tarjouspyynto = models.TextField()
    is_public   = models.BooleanField(('julkaistu'), default=False)
    mailed   = models.BooleanField(('toimitettu yritykseille'), default=False)

    def __unicode__(self):
	return self.otsikko
    def get_fields(self):
        return [(field.name, field.topic) for field in TarjousModel._meta.fields]

class TarjousModelForm(ModelForm):
    tarjoukset_viimeistaan = forms.DateField(widget=forms.DateInput(format = '%d.%m.%Y'), 
                                 input_formats=('%d.%m.%Y',))
   
    class Meta:
	model = TarjousModel
	fields = ('etunimi', 'sukunimi', 'email', 'puhelinnumero', 'toimiala', 'tarjoukset_viimeistaan','alue','otsikko','tarjouspyynto')
	widgets = {
	  'tarjouspyynto' : forms.Textarea(attrs={'rows':15, 'cols':50}),
	}
