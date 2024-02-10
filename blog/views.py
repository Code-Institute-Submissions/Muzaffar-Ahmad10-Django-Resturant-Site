from django.shortcuts import render
from django.http import HttpResponse
from blog.models import book_tabel

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
    if request.method == 'post':
        name = request.post.get('name')
        email = request.post.get('email')
        number = request.post.get('number')
        date = request.post.get('date')
        person = request.post.get('person')

        if name !='' and email !='' and number !='' and date !='' and person !='': 

            data = book_tabel(Name=name,Email=email,Number=number,Date=date,Person=person)
            data.save()
 

    return render(request,'reservation.html')        