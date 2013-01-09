# -*- coding: utf-8 -*-
from django.forms import ModelForm
from toimialakategoriat.models import Toimiala



class PhoneNoForm(ModelForm):
    class Meta:
        model = Toimiala
