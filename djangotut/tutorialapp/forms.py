from dataclasses import fields
import email
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *

from django.contrib.auth.models import User
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['firstname', 'lastname', 'middlename', 'grade']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = ['firstname', 'lastname', 'room_number', 'subject']

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']