from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path("", views.index, name='home'),
    path("second", views.second, name='second'), 
    path('contactsubmit', views.ContactSubmit, name='contact_submit'),
   
] 