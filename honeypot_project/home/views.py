from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    context ={
    "name":"ash"
    }
    return render(request,"home.html",context)
