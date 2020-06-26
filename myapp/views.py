from django.shortcuts import render, HttpResponse
from datetime import datetime
from django.contrib import messages
from django.conf import settings
from django.views import generic
from .models import Product, Contact


def index(request):
    prodscat1 = Product.objects.filter(category="1")
    #for i in prodscat1:
      #  print(i.product_name)
    prodscat2 = Product.objects.filter(category="2")
    prodscat3 = Product.objects.filter(category="3")
    allProducts = Product.objects.all()
    
    #prodscat.append([prodscat1,prodscat2,prodscat3])
    context= { 'allProducts':allProducts,   'prodscat1':prodscat1 , 'prodscat2':prodscat2 ,'prodscat3':prodscat3, 'ga_id': settings.GA_TRACKING_ID} 

    
    return render(request,'index.html', context)

    


def second(request):
   return render(request,'second.html')

def ContactSubmit(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date= datetime.today())
        contact.save()
        messages.success(request, 'one contact added !')
    return HttpResponse('your message has been sent !')