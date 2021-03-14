from django.shortcuts import render
from django.views import generic
from .forms import EntryForm
from .models import Entry
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class EntryCreateView(LoginRequiredMixin,generic.CreateView):
    
    model = Entry
    template_name = 'worklog/entry.html'
    form_class = EntryForm
    success_url = reverse_lazy('timesheet')

class EntryUpdateView(LoginRequiredMixin,generic.UpdateView):

    model = Entry
    template_name = 'worklog/entry.html'
    form_class = EntryForm
    success_url = reverse_lazy('timesheet')

class TimesheetView(LoginRequiredMixin,generic.ListView):

    context_object_name = 'timesheet_view'
    template_name = 'worklog/timesheet.html'

    def get_queryset(self):

        return Entry.objects.filter(employee_name=self.request.user).order_by('date')


class DiarysheetView(LoginRequiredMixin,generic.ListView):

    context_object_name = 'diarysheet_view'
    template_name = 'worklog/diarysheet.html'

    def get_queryset(self):

        return Entry.objects.all()

class TimesheetAdminListview(LoginRequiredMixin,generic.ListView):

    context_object_name = 'timesheet_admin_listview'
    template_name = 'worklog/timesheet_admin_listview.html'

class DiarysheetAdminListview(LoginRequiredMixin,generic.ListView):

    context_object_name = 'diarysheet_admin_listview'
    template_name = 'worklog/diarysheet_admin_listview.html'

