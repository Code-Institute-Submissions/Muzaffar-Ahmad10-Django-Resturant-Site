from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def my_blog(request):
    return render(request,'home.html')

def menu(request):
    return render(request,'menu.html') 

def gallery(request):
    return render(request,'gallery.html')          

def aboutus(request):
    return render(request,'aboutus.html') 

def signup(request):
    return render(request,'signup.html')

def reservation(request): 
    return render(request,'reservation.html')        