from django.http import HttpResponse
from django.http import JsonResponse
from apipkg import api_manager as api

import requests
import json

from django.shortcuts import redirect
from django.shortcuts import render

from django.core import serializers

from application.djangoapp.models import *
from django.views.decorators.csrf import csrf_exempt

from application.djangoapp.controller import promotions_customers as cutomers


# Display all target promotions for customers
def indexpromocustomers(request):
    data = PromotionsCustomers.objects.all()
    d = { 
            "list_promotions": data
        }
    return render(request, 'index_promo_customers.html', d)

# Dispatcher of targeted promotions customers resources
@csrf_exempt
def promoCustomers(request):
    if request.method == 'GET':
        return customers.index(request)
    return HttpResponse("The request has been failed")


# Compute targeted client Promotions
def calcPromoCustomers(request):
    # PromotionsEco.objects.all().delete()
    # count = ProductsEco.objects.count()
    # eco_random = ProductsEco.objects.all()[randint(0, count - 1)]
    
    # promo = randint(5, 15)
    # price = eco_random.prix - eco_random.prix * (promo / 100)
    # p = PromotionsEco(codeProduit = eco_random.codeProduit, familleProduit = eco_random.familleProduit,
    #                     descriptionProduit = eco_random.descriptionProduit, quantiteMin = eco_random.quantiteMin,
    #                     packaging = eco_random.packaging, prix = price, prixOriginel = eco_random.prix, reduction = promo)
    # p.save()
    
    # eco_random_2 = ProductsEco.objects.all()[randint(0, count - 1)]
    # while (eco_random_2 == eco_random):
    #     eco_random_2 = ProductsEco.objects.all()[randint(0, count - 1)]
    
    # promo = randint(5, 15)
    # price = eco_random_2.prix - eco_random_2.prix * (promo / 100)
    # p = PromotionsEco(codeProduit = eco_random_2.codeProduit, familleProduit = eco_random_2.familleProduit,
    #                     descriptionProduit = eco_random_2.descriptionProduit, quantiteMin = eco_random_2.quantiteMin,
    #                     packaging = eco_random_2.packaging, prix = price, prixOriginel = eco_random_2.prix, reduction = promo)
    # p.save()
    
    return render(request, 'home.html')