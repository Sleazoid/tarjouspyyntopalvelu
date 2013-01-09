from django.db import models
from django.forms import ModelForm
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)

    def __unicode__(self):
	return self.name

class ContactForm(ModelForm):
    class Meta:
	model = Contact
