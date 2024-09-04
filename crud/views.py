from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def teste(request):
    return render(request, "teste.html")