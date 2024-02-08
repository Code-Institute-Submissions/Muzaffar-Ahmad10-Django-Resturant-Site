from django.contrib import admin
from django.urls import path, include
from .views import my_blog
from .views import menu
from .views import gallery
from .views import aboutus
from .views import signup
from .views import reservation


urlpatterns = [
    path("", my_blog, name='blog'),
    path("menu/", menu, name='menu.html'),
    path("gallery/", gallery, name='gallery.html'),
    path("aboutus/", aboutus, name='aboutus.html'),
    path("signup/", signup, name='signup.html'),
    path("reservation/", reservation, name='reservation.html'),


]