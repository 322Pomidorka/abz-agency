from django import forms

from .models import Employees


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ['first_name', 'last_name', 'employment_position', 'employment_start_date', 'salary',
                  'employment_photo', 'parent'
                  ]
