from django.contrib import admin


from toimialakategoriat.models import Toimiala

class PhoneNoInline(admin.StackedInline):
    model = Toimiala
    extra = 0

class ContactAdmin(admin.ModelAdmin):
	inlines = [PhoneNoInline]


admin.site.register(Toimiala)



