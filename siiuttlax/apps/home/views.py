from django.shortcuts import render, redirect, render

# Create your views here.
def home(request):
    return render(request, 'home/home.html')