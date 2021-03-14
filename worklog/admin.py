from django.contrib import admin
from .models import Entry

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):

    list_display = ('job_number', 'client_name', 'project_ref', 'employee_name', 'hours', 'date', 'work_type', 'work_description',)