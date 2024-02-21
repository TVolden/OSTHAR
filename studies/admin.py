from django.contrib import admin

# Register your models here.
from .models import Study, Subject

class StudyAdmin(admin.ModelAdmin):
     list_display = ('pk', 'software', 'institution', 'trial', 'username')

admin.site.register(Study, StudyAdmin)
admin.site.register(Subject)