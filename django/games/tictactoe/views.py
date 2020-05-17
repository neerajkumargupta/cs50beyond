from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls  import reverse

class newGameForm(forms.Form):
    player1 = forms.CharField(label="Player1")
    player2 = forms.CharField(label="Player2")

def load(request):
    if "players" not in request.session:
        request.session["players"] = []
     
    if "board" not in request.session:
         request.session["board"] = [[None,None,None], [None,None,None], [None,None,None]]

    return render(request, "tictactoe/input.html", {
        "form": newGameForm()
    })


def index(request):
    if "players" not in request.session:
        request.session["players"] = []
     
    if "board" not in request.session:
         request.session["board"] = [[None,None,None], [None,None,None], [None,None,None]]

    if request.method == "POST":
        form = newGameForm(request.POST)
        if form.is_valid():
            player1 = form.cleaned_data["player1"]
            player2 = form.cleaned_data["player2"]
            request.session["players"] += [player1,player2]
            request.session["turn"] = player1
            print(f" value for player1 and 2 {player1}  {player2} ### {request} ### {request.session.items()}")
            return HttpResponseRedirect(reverse("tictactoe:gameboard"))
        else:
             return render(request, "tictactoe/input.html", {
            "form": form
            })

    return render(request, "tictactoe/input.html", {
        "form": newGameForm()
    })

def gameboard(request):
        print(f"play current value of in session {request.session.items()}")
        return render(request, "tictactoe/game.html",{
            "range":range(3),
            "game":request.session["board"]
        })
