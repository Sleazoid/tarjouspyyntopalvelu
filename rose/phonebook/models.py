# -*- coding: utf-8 -*-

from django.db import models
from django import forms
from django.forms import ModelForm
from django.forms.widgets import *
from django.contrib import admin

		
class Toimiala(models.Model):
    
    toimiala = models.CharField(max_length=20)
    

    def __unicode__(self):

        return self.toimiala
class ChoiceInline(admin.TabularInline):
    model = Toimiala
    extra = 0
class Contact(models.Model):
    LAPPI = 'LA'
    AHVENANMAA = 'AH'
    ETELAPOHJANMAA = 'EP'
    ETELASAVO = 'ES'
    KAINUU = 'KA'
    KANTAHAME = 'KH'
    KESKIPOHJANMAA ='KP'
    KESKISUOMI ='KS'
    KYMENLAAKSO ='KY'
    PIRKANMAA ='PI'
    POHJANMAA ='PO'
    POHJOISKARJALA ='PK'
    POHJOISPOHJANMAA ='PP'
    POHJOISSAVO ='PS'
    PAIJATHAME ='PH'
    SATAKUNTA = 'SA'
    UUSIMAA ='UU'
    VARSINAISSUOMI ='VS'

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
    etunimi = models.CharField(max_length=80)
    sukunimi = models.CharField(max_length=80)
    email = models.EmailField(max_length=80)
    maakunta = models.CharField(max_length=2,
				choices=LAANIT_CHOICES,
				default=LAPPI)
    puhelinnumero = models.CharField(max_length=20)
    toimiala = models.ForeignKey(Toimiala)
    inlines = [ChoiceInline]
    seloste = models.TextField()
    def __unicode__(self):
       
	#return self.(sukunimi, etunimi)
	return '%s %s' % (self.etunimi, self.sukunimi)


