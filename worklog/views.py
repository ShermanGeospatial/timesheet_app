from django.shortcuts import render
from django.views import generic
from .forms import EntryForm
from .models import Entry
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
import itertools

class EntryCreateView(LoginRequiredMixin,generic.CreateView):
    
    model = Entry
    template_name = 'worklog/entry.html'
    form_class = EntryForm
    success_url = reverse_lazy('timesheet')

    def form_valid(self, form):

        instance = form.save(commit=False)
        form.instance.employee_name = self.request.user
        form.save()
        return super(EntryCreateView, self).form_valid(form)

class EntryUpdateView(LoginRequiredMixin,generic.UpdateView):

    model = Entry
    template_name = 'worklog/entry.html'
    form_class = EntryForm
    success_url = reverse_lazy('timesheet')

    def form_valid(self, form):

        instance = form.save(commit=False)
        form.instance.employee_name = self.request.user
        form.save()
        return super(EntryUpdateView, self).form_valid(form)

class TimesheetView(LoginRequiredMixin,generic.ListView):

    context_object_name = 'timesheet_view'
    template_name = 'worklog/timesheet.html'

    def get_queryset(self):

        entry_log = Entry.objects.filter(employee_name=self.request.user).order_by('date').order_by('job_number')

        for log in entry_log:

            print(log.date.day)

        return entry_log

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

