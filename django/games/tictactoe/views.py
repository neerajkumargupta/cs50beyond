from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls  import reverse

class newGameForm(forms.Form):
    player1 = forms.CharField(label="Player1")
    player2 = forms.CharField(label="Player2")

def load(request):
    return render(request, "tictactoe/input.html", {
        "form": newGameForm()
    })


def play(request):
    if request.method == "POST":
        form = newGameForm(request.POST)
        if form.is_valid():
            player1 = form.cleaned_data["player1"]
            player2 = form.cleaned_data["player2"]
            print(" value for player1 and 2 ")
            request.session["players"] += [player1,player2]
            request.session["board"] = [[None,None,None], [None,None,None], [None,None,None]]

            return HttpResponseRedirect(reverse("tictactoe:game"))
        else:
             return render(request, "tictactoe/input.html", {
            "form": form
            })

    return render(request, "tictactoe/input.html", {
        "form": newGameForm()
    })


