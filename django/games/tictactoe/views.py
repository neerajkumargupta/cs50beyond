from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls  import reverse

class newGameForm(forms.Form):
    player1 = forms.CharField(label="Player1")
    player2 = forms.CharField(label="Player2")

def load(request):
    return render(request, "tictactoe/input.html")

def index(request):
    if "players" not in request.session:
        request.session["players"] = []

    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        form = newTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
             return render(request, "tasks/add.html", {
            "form": form
            })

    return render(request, "tasks/add.html", {
        "form": newTaskForm()
    })


