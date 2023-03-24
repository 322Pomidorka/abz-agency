from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_employees, name='show_employees'),
    path('employees', views.full_info_employees, name='employees_full')
]
