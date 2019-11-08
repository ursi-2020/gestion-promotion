from django.http import HttpResponse
from django.http import JsonResponse
from apipkg import api_manager as api


from django.shortcuts import redirect
from django.shortcuts import render
import requests
from application.djangoapp.models import *


# this function clear all databases
def clear(request):
    PromotionsMag.objects.all().delete()
    PromotionsEco.objects.all().delete()
    PromotionsCustomers.objects.all().delete()
    PromotionsCustomersProducts.objects.all.delete()

    ProductsMag.objects.all().delete()
    ProductsEco.objects.all().delete()  
    Products.objects.all().delete()

    Customers.objects.all().delete()
    Tickets.objects.all().delete()
    return render(request, 'home.html')

# Home page
def home(request):
    return render(request, 'home.html')




