from email import message
from telnetlib import theNULL
from django.shortcuts import redirect, render
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import *

def home(request):
    return render(request, 'defaultApp/home.html')

@login_required(login_url='login')
def staffView(request):
    tasks = Task.objects.all()
    departments = Department.objects.all()

    combinedList = tasks.values_list
    return render(request, 'defaultApp/staff.html', {'tasks' : tasks})

def loginUser(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request,"Login details incorrect")
            return render(request, 'defaultApp/login.html')

    context = {}
    return render(request, 'defaultApp/login.html', context)
    

def logoutUser(request):
    logout(request)
    return redirect("login")
