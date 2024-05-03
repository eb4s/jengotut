from dataclasses import fields
import email
from django import forms
from django.contrib.auth.forms. import UserCreationForm

from .models import *

from django.contrib.auth.models import User
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['firstname', 'lastname', 'middlename', 'grade']

class teacherForm(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = ['firstname', 'lastname', 'room_number', 'subject']

class RegistrationForm(forms.UserCreationForm):
    email = forms.EmailFeild(required = True)
    class Meta:
        model = User
        feilds = ['username', 'email', 'password1', 'password2']