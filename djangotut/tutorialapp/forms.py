from dataclasses import fields
from django import forms

from .models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['firstname', 'lastname', 'middlename', 'grade']

class teacherForm(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = ['firstname', 'lastname', 'room_number', 'subject']
