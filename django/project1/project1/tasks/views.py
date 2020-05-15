from django.shortcuts import render
from django import forms

tasks = ["foo", "bar", "baz"]
# Create your views here.

class newTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def add(request):
    return render(request, "tasks/add.html", {
        "form": newTaskForm()
    })


