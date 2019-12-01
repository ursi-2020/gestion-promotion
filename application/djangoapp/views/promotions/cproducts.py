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
from datetime import datetime, timedelta

from application.djangoapp.controller import promotions_cproducts as cproducts

# Display all target promotions for customers
def indexpromocustomersproducts(request):
    data = PromotionsCustomersProducts.objects.all()
    d = { 
            "list_promotions": data
        }
    return render(request, 'index_promo_cproducts.html', d)

# Dispatcher of targeted promotions customers resources
@csrf_exempt
def promoCustomersProducts(request):
    if request.method == 'GET':
        return cproducts.index(request)
    return HttpResponse("The request has been failed")


# Compute targeted client Promotions
@csrf_exempt
def calcPromoCustomersProducts(request):
    clock_time = api.send_request('scheduler', 'clock/time')
    time = datetime.strptime(clock_time, '"%d/%m/%Y-%H:%M:%S"')
    time = time - timedelta(weeks=1)
    for t in Tickets.objects.filter(date__gte = time):
        for pt in t.articles.all():
            if PromotionsCustomersProducts.objects.filter(IdClient = t.client, codeProduit = pt.codeProduit, date__gte = time).count() == 0:
                new_promo = PromotionsCustomersProducts(date = time + timedelta(weeks=1), IdClient = t.client, codeProduit = pt.codeProduit, quantity = pt.quantity)
                new_promo.save()
            else:
                if PromotionsCustomersProducts.objects.all().count() > 0:
                    try:
                        promo = PromotionsCustomersProducts.objects.get(IdClient = t.client, codeProduit = pt.codeProduit, date__gte = time + timedelta(weeks=1))
                        promo.quantity += pt.quantity
                        promo.save()
                    except PromotionsCustomersProducts.DoesNotExist:
                        promo = None
    if PromotionsCustomersProducts.objects.all().count() > 0:
        little_promo = PromotionsCustomersProducts.objects.filter(quantity__gte = 3, date__gte = time + timedelta(weeks=1)).exclude(quantity__gt = 4)
        big_promo = PromotionsCustomersProducts.objects.filter(quantity__gte = 5, date__gte = time + timedelta(weeks=1))

        for lp in little_promo:
            lp.reduction = 10
            product = Products.objects.get(codeProduit = lp.codeProduit)
            if (product.prixFournisseur > product.prix - product.prix * lp.reduction / 100):
                price = product.prixFournisseur + 1
                lp.reduction = price * 100 / product.prix
                lp.reduction = 100 - lp.reduction
            lp.save()

        for bp in big_promo:
            bp.reduction = 25
            product = Products.objects.get(codeProduit = bp.codeProduit)
            if (product.prixFournisseur > product.prix - product.prix * bp.reduction / 100):
                price = product.prixFournisseur + 1
                bp.reduction = price * 100 / product.prix
                bp.reduction = 100 - bp.reduction
            bp.save()

    return render(request, 'home.html')