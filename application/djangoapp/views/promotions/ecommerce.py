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
    return render(request, 'index_promo_eco.html', d)

# Dispatcher of promotion ecommerce resources
@csrf_exempt
def promoEco(request):
    if request.method == 'GET':
        return eco.index(request)
    return HttpResponse("The request has been failed")

# Compute Ecommerce Promotions
@csrf_exempt
def calcPromoEco(request):
    # PromotionsEco.objects.all().delete()
    clock_time = api.send_request('scheduler', 'clock/time')
    time = datetime.strptime(clock_time, '"%d/%m/%Y-%H:%M:%S"')

    count = ProductsEco.objects.count()
    eco_random = ProductsEco.objects.all()[randint(0, count - 1)]
    
    promo = randint(5, 15)
    price = eco_random.prix - eco_random.prix * (promo / 100)
    if (eco_random.prixFournisseur > price):
        price = eco_random.prixFournisseur + 1
        promo = price * 100 / eco_random.prix
        promo = 100 - promo
    p = PromotionsEco(codeProduit = eco_random.codeProduit, familleProduit = eco_random.familleProduit,
                        descriptionProduit = eco_random.descriptionProduit, quantiteMin = eco_random.quantiteMin,
                        packaging = eco_random.packaging, prix = price, prixOriginel = eco_random.prix, reduction = promo, date = time)
    p.save()
    
    eco_random_2 = ProductsEco.objects.all()[randint(0, count - 1)]
    while (eco_random_2 == eco_random):
        eco_random_2 = ProductsEco.objects.all()[randint(0, count - 1)]
    
    promo = randint(5, 15)
    price = eco_random_2.prix - eco_random_2.prix * (promo / 100)
    if (eco_random_2.prixFournisseur > price):
        price = eco_random_2.prixFournisseur + 1
        promo = price * 100 / eco_random.prix
        promo = 100 - promo
    p = PromotionsEco(codeProduit = eco_random_2.codeProduit, familleProduit = eco_random_2.familleProduit,
                        descriptionProduit = eco_random_2.descriptionProduit, quantiteMin = eco_random_2.quantiteMin,
                        packaging = eco_random_2.packaging, prix = price, prixOriginel = eco_random_2.prix, reduction = promo, date = time)
    p.save()
    
    return render(request, 'home.html')