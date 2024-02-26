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

#about us page rendering
def about_us_page(request):
    return render(request, 'about-us.html')


#Booking page functionality
@login_required(login_url="/login/")
def booking_page(request):
    if request.method == "POST":
        person_name = request.POST.get('person-name')
        person_number = request.POST.get('phone-number')
        person_email = request.POST.get('person-email')
        guest_count = request.POST.get('guest-count')
        guest_table = request.POST.get('guest-table')
        requested_date = request.POST.get('requested-date')
        requested_time = request.POST.get('requested-time')

        if guest_count == "Guests Selection":
            messages.error(request, "Please select the right guest count.")
            return redirect('booking_page')
        if guest_table == "Tables Selection":
            messages.error(request, "Please select the right table.")
            return redirect('booking_page')

        current_user = request.user
        Booking.objects.create(
            user=current_user,
            person_name=person_name,
            person_email=person_email,
            person_number=person_number,
            guest_count=guest_count,
            guest_table=guest_table,
            requested_date=requested_date,
            requested_time=requested_time
        )
        messages.success(request, "Your table has been successfully reserved.")
        return redirect('booking_page')

    return render(request, 'booking.html')


#checking user it own tables and bookings
@login_required(login_url="/login/")
def my_booking(request):
    user = request.user
    user_bookings = Booking.objects.filter(user=user)

    if request.method == 'POST':
        try:
            if "edit-booking" in request.POST:
                booking_id = request.POST.get('edit-booking-id')
                get_booking = Booking.objects.get(id=booking_id)

                person_name = request.POST.get('person-name')
                person_number = request.POST.get('person-number')
                person_email = request.POST.get('person-email')
                guest_count = request.POST.get('guest-count')
                guest_table = request.POST.get('guest-table')
                requested_date = request.POST.get('requested-date')
                requested_time = request.POST.get('requested-time')

                get_booking.person_name = person_name
                get_booking.person_email = person_email
                get_booking.person_number = person_number
                get_booking.guest_count = guest_count
                get_booking.guest_table = guest_table
                get_booking.requested_date = requested_date
                get_booking.requested_time = requested_time

                get_booking.save()
                messages.success(request, "Your table reservation has been edited successfully")
                return redirect('my_booking')
            elif "delete-booking" in request.POST:
                booking_id = request.POST.get('delete-booking-id')
                get_booking = Booking.objects.get(id=booking_id)
                get_booking.delete()
                messages.success(request, "Your table reservation has been deleted successfully.")
                return redirect('my_booking')
        except:
            messages.error(request, "Something went wrong, Please try again.")
            return redirect('my_booking')

    context = {'bookings': user_bookings}
    return render(request, 'my-booking.html', context)