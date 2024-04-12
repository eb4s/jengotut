from multiprocessing import context
from django.shortcuts import render
from .models import *



# Create your views here.

def base(request):
    context={

    }

    return render(request, 'base.html', context)

def home(request):
    context={

    }

    return render(request, 'home.html', context)

def students(request):
    students = Student.objects.all() #gets all records and saves to a students list
    context={
        'students' :students, #exports students list to the template(webpage)
    }

    return render(request, 'students.html', context)


def teachers(request):
    teachers = Teachers.objects.all() #gets all records and saves to a students list
    context={
        'teachers' :teachers, #exports students list to the template(webpage)
    }

    return render(request, 'teachers.html', context)