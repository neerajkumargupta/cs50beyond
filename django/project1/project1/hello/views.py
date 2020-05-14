from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, How are you World!")

def neeraj(request):
    return HttpResponse("Hello, How are you Neeraj!!")

def greet(request , name):
    return render(request,"hello/greet.html",{
        "name": name.capitalize()
    })
