from operator import imod
from turtle import title

import django
from todoapp.models import Task
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http.response import HttpResponse;
# from django.views.generic.list import ListView;
from todoapp.models import Task;
from .forms import CreateTask,UpdateTask,CreateUser;
from django.contrib.auth.models import User;
from django.contrib import auth,messages;


# Create your views here.
def taskList(request):
    user = auth.get_user(request);
    
    if user.is_authenticated:
        tasks = Task.objects.filter(user=auth.get_user(request));
        form = CreateUser()
        if request.method == "POST":
            form = CreateUser(request.POST);
            if form.is_valid():
                    form.save();       
        return render(request,"task_list.html",{"tasks":tasks,"form":form});
    else:
        return render(request,"task_list.html");

# class TaskList(ListView):
#     model = Task
#     context_object_name = "tasks"


def specific_task(request,pk):
    specificTask = Task.objects.get(id=pk);
    return render(request,"specific_task.html",{"task":specificTask});

def create_task(request):
    form = CreateTask();
    if request.method == "POST":
        form = CreateTask(request.POST);
        if form.is_valid():
            user = auth.get_user(request)
            
            Task.objects.create(user = user,title=form.cleaned_data["title"],description = form.cleaned_data["description"]);
            return redirect('/')
            
    return render(request,"create_task.html",{"form":form});

def update_task(request,pk):
    task = Task.objects.get(id=pk);
    form = UpdateTask(instance=task)
    if request.method=="POST":
        form =UpdateTask(request.POST,instance=task);
        if form.is_valid():
            form.save();
            return redirect('/')
    
    return render(request,"update_task.html",{"form":form});


def task_delete(request,pk):
    task = Task.objects.get(id=pk);
    task.delete();
    return redirect('/')

def login_user(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return render(request,'login.html')  

    else:
        return render(request,'login.html')  

def register_user(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return render(request,'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return render(request,'register.html')
            else:   
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save();
                
                return render(request,'login.html')  

        else:
            messages.info(request,'password not matching..')    
            return render(request,'register.html')
        
        
    else:
        return render(request,'register.html')


def logout(request):
    auth.logout(request)
    return render(request,"task_list.html");


    
   