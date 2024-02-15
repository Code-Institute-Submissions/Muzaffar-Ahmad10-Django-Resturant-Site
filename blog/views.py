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
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        date = request.POST.get('date')
        person = request.POST.get('person')

        if name !='' and email !='' and number !='' and date !='' and person !='': 

            data = book_tabel(Name=name,Email=email,Number=number,Date=date,Person=person)
            print(data)
            data.save()
 

    return render(request,'reservation.html')        