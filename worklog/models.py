from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):

    job_number = models.IntegerField()
    client_name = models.CharField(max_length=100)
    project_ref = models.CharField(max_length=100)
    employee_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    hours = models.FloatField()
    date = models.DateField()
    work_type = models.CharField(max_length=100)
    work_description = models.TextField()
