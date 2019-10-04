from django.http import HttpResponse
from django.http import JsonResponse
from apipkg import api_manager as api

import requests
import json

from django.shortcuts import redirect
from django.shortcuts import render

from django.core import serializers
from random import randint

from application.djangoapp.models import *
from django.views.decorators.csrf import csrf_exempt

from application.djangoapp.controller import promotions_eco as eco

# Display all promotions for ecommerce
def indexpromoeco(request):
    data = PromotionsEco.objects.all()
    d = { 
            "list_products": data
        }
    return render(request, 'index_product_eco.html', d)

# Dispatcher of promotion ecommerce resources
@csrf_exempt
def promoEco(request):
    if request.method == 'GET':
        return eco.index(request)
    return HttpResponse("The request has been failed")

# Compute Ecommerce Promotions
def calcPromoEco(request):
    PromotionsEco.objects.all().delete()
    count = ProductsEco.objects.count()
    eco_random = ProductsEco.objects.all()[randint(0, count - 1)]
    
    promo = randint(5, 15)
    price = eco_random.prix - eco_random.prix * (promo / 100)
    p = PromotionsEco(codeProduit = eco_random.codeProduit, familleProduit = eco_random.familleProduit,
                        descriptionProduit = eco_random.descriptionProduit, quantiteMin = eco_random.quantiteMin,
                        packaging = eco_random.packaging, prix = price)
    p.save()
    
    eco_random_2 = ProductsEco.objects.all()[randint(0, count - 1)]
    while (eco_random_2 == eco_random):
        eco_random_2 = ProductsEco.objects.all()[randint(0, count - 1)]
    
    promo = randint(5, 15)
    price = eco_random_2.prix - eco_random_2.prix * (promo / 100)
    p = PromotionsEco(codeProduit = eco_random_2.codeProduit, familleProduit = eco_random_2.familleProduit,
                        descriptionProduit = eco_random_2.descriptionProduit, quantiteMin = eco_random_2.quantiteMin,
                        packaging = eco_random_2.packaging, prix = price)
    p.save()
    
    return HttpResponse("The two promos were successfully created")