from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.http import HttpResponse
from .models import *
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    students = Student.objects.all()
    context = {'students': students}
    return render (request,'home.html',context=context)

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def StudentinfoPage(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'studentinfo.html',context=context)

login_required
def ChangepassPage(request):
    if request.method == 'POST':
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Passwords do not match!")
        else:
            user = request.user
            user.set_password(pass1)  # Proper way to change password
            user.save()
            update_session_auth_hash(request, user)  # Keeps user logged in
            return redirect('login')  # Or wherever you want to redirect
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'changepass.html',context=context)

def AdmitcardPage(request):
    students = Student.objects.all()
    registers = CourseRegister.objects.all()
    context = {'registers': registers, 
               'students': students}
    return render (request,'admitcard.html',context=context)


def CourseregisterPage(request):
    registers = CourseRegister.objects.all()
    students = Student.objects.all()
    context = {'registers': registers, 
               'students': students}
    return render(request, 'courseregister.html',context=context)


def ResultPage(request):
    students = Student.objects.all()
    context = {'students': students}
    return render (request,'result.html',context=context)






    