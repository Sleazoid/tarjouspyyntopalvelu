from django.contrib import admin

from phonebook.models import Contact
from phonebook.models import Toimiala

class PhoneNoInline(admin.StackedInline):
    model = Toimiala
    extra = 0

class ContactAdmin(admin.ModelAdmin):
	inlines = [PhoneNoInline]


admin.site.register(Toimiala)



