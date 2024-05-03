from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from .forms import StudentForm
from .models import *
from .forms import *
from django.contrib import messages



# Create your views here.

def registerPage(request):
    form = UserCreationForm
    context={}

    return render(request, 'register.html', context)





def loginPage(request):
    form = UserCreationForm
    context={}

    return render(request, 'login.html', context)






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


def teacherform(request):
    context={}
    if request.method == "POST": #check for button click
        form = teacherForm(request.POST)
        if form.is_valid():
            context=""
            for name, value in form.cleaned_data.items():
                print("{}: ({} {}".format\
                (name, type(value), value))
        #save data locally but not to the database yet
        requests = form.save(commit=False) #captures all data entered in form and saves to a requests list object


        #save each field to local variable
        firstname = form.cleaned_data['firstname']
        lastname = form.cleaned_data['lastname']
        room_number = form.cleaned_data['room_number']
        subject = form.cleaned_data['subject']         
        requests.save() #save to the database

        messages.success(request, "New Teacher Added Succesfully!")


    else:
        form = teacherForm()
    #return the form and all of it fi
    return render(request, "teacherform.html", \
        {"method": request.method, "form": form}
        )


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

        messages.success(request, "New Student Added Succesfully!")



    else: #if they havnt pressed butoon let them view blank form
        form = StudentForm()
    return render(request, 'studentform.html', \
        {'method': request.method, 'form': form}
        )

def register(request):
    form = RegistrationForm
    if request.method== 'POST':
        form = RegistrationForm(request.post)
        if form.is_valid():
            user = form.save()
            login(request.user)
            return redirect('')
        else:
            form = RegistrationForm()
    return render(request, "registration.html", {'form' :form})