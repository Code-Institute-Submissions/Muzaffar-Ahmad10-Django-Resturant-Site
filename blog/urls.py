from django.contrib import admin
from django.urls import path, include
from .views import my_blog
from .views import menu
from .views import gallery
from .views import aboutus
from .views import signup
from .views import reservation


urlpatterns = [
    path("", my_blog, name='home'),
    path("menu/", menu, name='menu'),
    path("gallery/", gallery, name='gallery'),
    path("aboutus/", aboutus, name='aboutus'),
    path("signup/", signup, name='signup'),
    path("reservation/", reservation, name='reservation'),


]