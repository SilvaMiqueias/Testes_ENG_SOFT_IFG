from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, "index.html")

@login_required
def teste(request):
    return render(request, "teste.html")