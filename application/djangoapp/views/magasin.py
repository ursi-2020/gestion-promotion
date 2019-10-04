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

from application.djangoapp.controller import promotions_mag as mag

# Display all promo for magasin
def indexpromomag(request):
    data = PromotionsMag.objects.all()
    d = { 
            "list_products": data
        }
    return render(request, 'index_product_mag.html', d)

# Dispatcher of promotion magasin resources
@csrf_exempt
def promoMag(request):
    if request.method == 'GET':
        return mag.index(request)
    return HttpResponse("The request has been failed")

# Compute Magasin Promotions
def calcPromoMag(request):
    PromotionsMag.objects.all().delete()
    count = ProductsMag.objects.count()
    eco_random = ProductsMag.objects.all()[randint(0, count - 1)]
    
    promo = randint(5, 15)
    price = eco_random.prix - eco_random.prix * (promo / 100)
    p = PromotionsMag(codeProduit = eco_random.codeProduit, familleProduit = eco_random.familleProduit,
                        descriptionProduit = eco_random.descriptionProduit, quantiteMin = eco_random.quantiteMin,
                        packaging = eco_random.packaging, prix = price)
    p.save()
    
    eco_random_2 = ProductsMag.objects.all()[randint(0, count - 1)]
    while (eco_random_2 == eco_random):
        eco_random_2 = ProductsMag.objects.all()[randint(0, count - 1)]
    
    promo = randint(5, 15)
    price = eco_random_2.prix - eco_random_2.prix * (promo / 100)
    p = PromotionsMag(codeProduit = eco_random_2.codeProduit, familleProduit = eco_random_2.familleProduit,
                        descriptionProduit = eco_random_2.descriptionProduit, quantiteMin = eco_random_2.quantiteMin,
                        packaging = eco_random_2.packaging, prix = price)
    p.save()
    
    return HttpResponse("The two promos were successfully created")