from tyopaikat.models import TyopaikkaModel
from tyopaikat.models import TyopaikkaModelForm

#from forms import CommentForm
from django.contrib import admin
#from formadmin import sites

class TyopaikkaModelAdmin(admin.ModelAdmin):
    form = TyopaikkaModelForm
    list_display = ['otsikko', 'toimiala','etunimi','sukunimi']

#class CommentFormAdmin(admin.ModelForm):
#	nimi = 'nimi'
#	email = 'email'
#sites.register(CommentForm, CommentFormAdmin)

admin.site.register(TyopaikkaModel,TyopaikkaModelAdmin)

