from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *


#homepage rendering
def homepage(request):
    return render(request, 'homepage.html')


# Signup Functionality
def user_signup(request):
    if request.method == 'POST':
        # Get form data from POST request
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("password1")
        
        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        # Check if username is already taken
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return redirect('signup')

        # Check if email is already in use
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already used, please enter your own email!")
            return redirect('signup')

        # Create new user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, "Account created successfully. You can now login.")
        return redirect('login')
    else:
        return render(request, 'signup.html')
    
def user_login(request):
    if request.method == 'POST':
        # Get form data from POST request
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        # Check if authentication was successful
        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in.")
            return redirect('homepage')  # Redirect to home or any other page after login
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')

def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        if email and message:
            contact_form = ContactUs.objects.create(name=name, email=email, message=message)
            messages.success(request, "Successfully submitted the form. We typically reply within 2 hours.")
            return redirect('contact_us')
        else:
            messages.error(request, "Error submitting the form, please try again.")
            return redirect('contact_us')

    return render(request, 'contact-us.html')

#food menu
def food_menu(request):
    return render(request, 'food-menu.html')

#drink menu
def drinks_menu(request):
    return render(request, 'drinks-menu.html')