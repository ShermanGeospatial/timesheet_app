from django.forms import ModelForm
from .models import Entry

class EntryForm(ModelForm):
    
    class Meta:
        model = Entry
        fields = [
            'job_number', 
            'client_name', 
            'project_ref', 
            'employee_name', 
            'hours', 
            'date', 
            'work_type', 
            'work_description',
        ]
        #widgets = {}