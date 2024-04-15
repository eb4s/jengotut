from multiprocessing import context
from django.shortcuts import render

from .forms import StudentForm
from .models import *
from .forms import *



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

def studentform(request):
    context={}
    if request.method == "POST": #check for button press
        form = StudentForm(request.POST)
        if form.is_valid():
            context = ""
            for name, value in form.cleaned_data.items():
                print ("{}: ({} {}" .format\
                    (name, type(value), value))

        requests = form.save(commit=False)

        firstname = form.cleaned_data['firstname']
        lastname = form.cleaned_data['lastname']
        middlename = form.cleaned_data['middlename']
        grade = form.cleaned_data['grade']
        requests.save()
    else: #if they havnt pressed butoon let them view blank form
        form = StudentForm()
    return render(request, 'studentform.html', \
        {'method': request.method, 'form': form}
        )