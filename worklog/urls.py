from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:pk>/', views.EntryUpdateView.as_view(), name="entry_update"),
    path('new/', views.EntryCreateView.as_view(), name="entry_create"),
    path('timesheet/', views.TimesheetView.as_view(),name="timesheet"),
]