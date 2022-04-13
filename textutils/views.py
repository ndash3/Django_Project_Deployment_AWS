from django import views
from django.shortcuts import render
from .forms import ApplicationForm

def index(request):
    form = ApplicationForm()
    return render(request, 'app/homepage.html', {'forms':form})