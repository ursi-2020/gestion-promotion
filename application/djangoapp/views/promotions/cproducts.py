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

from application.djangoapp.controller import promotions_cproducts as cproducts

# Display all target promotions for customers
def indexpromocustomersproducts(request):
    data = PromotionsCustomersProducts.objects.all()
    d = { 
            "list_promotions": data
        }
    return render(request, 'index_promo_customers.html', d)

# Dispatcher of targeted promotions customers resources
@csrf_exempt
def promoCustomersProducts(request):
    if request.method == 'GET':
        return cproducts.index(request)
    return HttpResponse("The request has been failed")


# Compute targeted client Promotions
def calcPromoCustomersProducts(request):
    PromotionsCustomersProducts.objects.all().delete()
    tickets = Tickets.objects.all()
    for t in tickets:
        for pt in t['articles']:
            if PromotionsCustomersProducts.objects.filter(IdClient = t.client, codeProduit = pt.codeProduit).count() == 0:
                new_promo = PromotionsCustomersProducts(IdClient = t.client, codeProduit = pt.codeProduit, quantity = pt.quantity)
            else:
                promo = PromotionsCustomersProducts.get(IdClient = t.client, codeProduit = pt.codeProduit)
                promo.quantity += pt.quantity
                promo.save()
    
    little_promo = PromotionsCustomersProducts.objects.filter(quantity__gte = 3).exclude(quantity__lte = 4)
    big_promo = PromotionsCustomers.objects.filter(quantity__gte = 5)

    for lp in little_promo:
        lp.reduction = 10
        lp.save()

    for bp in big_promo:
        bp.reduction = 25
        bp.save()

    return render(request, 'home.html')