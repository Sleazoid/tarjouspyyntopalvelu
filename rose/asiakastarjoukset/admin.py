from asiakastarjoukset.models import Poll
from asiakastarjoukset.models import Choice
from django.contrib import admin
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
admin.site.register(Poll, PollAdmin)

