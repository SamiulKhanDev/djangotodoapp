from dataclasses import fields
from pyexpat import model
from django import forms;
from .models import Task;
from django.contrib.auth.models import User

class CreateTask(forms.ModelForm):
    class Meta:
        model = Task;
        fields = (
            
            'title',
            'description',
           

        )

class UpdateTask(forms.ModelForm):
    class Meta:
        model = Task;
        fields = (
            
            'title',
            'description',
            'complete'
           

        )

class CreateUser(forms.ModelForm):
    class Meta:
        model = User;
        fields=(
            'username',
            'password',
        )

