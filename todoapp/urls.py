
from urllib.request import parse_http_list
from django import views
from .views import taskList,specific_task,create_task,update_task,task_delete,login_user,register_user,logout;
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',taskList,name="TaskList"),
    path("task/<int:pk>",specific_task,name="specific_task"),
    path("createTask",create_task,name="create_task"),
    path("task/update/<int:pk>",update_task,name = "update_task"),
    path("task/delete/<int:pk>",task_delete,name="task_delete"),
    path("login",login_user,name="login_user"),
    path("register", register_user, name="register"),
    path("logout",logout,name="logout"),

    
   
]
