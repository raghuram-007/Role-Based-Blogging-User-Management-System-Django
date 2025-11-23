# blogs/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_post, name='create_post'),
    path('my-posts/', views.my_posts, name='my_posts'),
    path('posts/', views.patient_posts, name='patient_posts'),
   
]
