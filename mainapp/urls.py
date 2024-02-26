from django.urls import path
from .views import *

urlpatterns = [
    path("", homepage, name="homepage"),
    path("signup/", user_signup, name="signup"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("contact-us/", contact_us, name="contact_us"),
    path("food-menu/", food_menu, name="food_menu"),
    path("drinks-menu/", drinks_menu, name="drinks_menu"),
    path("about-us/", about_us_page, name="about_us_page"),
    path("booking/", booking_page, name="booking_page"),
    path("my-booking/", my_booking, name="my_booking"),
    
]