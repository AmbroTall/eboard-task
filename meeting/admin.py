from django.contrib import admin

from .models import Minutes, Meeting, Document, Agenda

admin.site.register(Meeting)
admin.site.register(Minutes)
admin.site.register(Document)
admin.site.register(Agenda)
