
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from userena.models import UserenaBaseProfile
from phonebook.models import PhoneNo
class GProfile(models.Model):
    # This is the only required field
    user = models.ForeignKey(User, unique=True)

    # The rest is completely up to you...
    
    etunimi = models.CharField(max_length=100, blank=True)
    sukunimi = models.CharField(max_length=100, blank=True)
    toimiala = models.CharField(max_length=100, blank=True)


class MyProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=('user'),
                                related_name='my_profile')
    toimiala = models.ModelChoiceField(queryset=PhoneNo.objects.all())
    favourite_snack = models.CharField(('favourite snack'),
                                       max_length=5)
    name = models.CharField(('Name of the project'), max_length=100)
