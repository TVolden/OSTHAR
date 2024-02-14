from django.contrib import admin
from .models import Record

# Register your models here.
class RecordAdmin(admin.ModelAdmin):
    list_display = ('pk', 'servertime', 'behavior', 'affect', 'marked', 'note')

admin.site.register(Record, RecordAdmin)