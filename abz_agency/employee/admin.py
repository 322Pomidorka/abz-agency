from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import *


class EmployeeAdmin(MPTTModelAdmin):
    prepopulated_fields = {"first_name": ("first_name",)}


admin.site.register(Employees, EmployeeAdmin)



