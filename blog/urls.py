from django.urls import path
from .views import *

urlpatterns = [
    path('posts/', blog_post_list, name='blog_post_list'),
    path('post/<int:id>/', single_post, name='single_post'),
]