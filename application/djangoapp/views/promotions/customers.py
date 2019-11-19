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

from application.djangoapp.controller import promotions_customers as customers

# Display all target promotions for customers
def indexpromocustomers(request):
    data = PromotionsCustomers.objects.all()
    print(data[0].reduction)
    d = { 
            "list_promotions": data
        }
    print("lol")
    return render(request, 'index_promo_customers.html', d)

# Dispatcher of targeted promotions customers resources
@csrf_exempt
def promoCustomers(request):
    if request.method == 'GET':
        return customers.index(request)
    return HttpResponse("The request has been failed")


# Compute targeted client Promotions
@csrf_exempt
def calcPromoCustomers(request):
    # PromotionsCustomers.objects.all().delete()
    clock_time = api.send_request('scheduler', 'clock/time')
    time = datetime.strptime(clock_time, '"%d/%m/%Y-%H:%M:%S"')
    time = time - timedelta(weeks=1)
    loop = 1
    for t in Tickets.objects.all():
        tk = Tickets.objects.filter(client = t.client, date__gte = time).count()
        if loop == 1:
            if tk > 10 and PromotionsCustomers.objects.filter(IdClient = t.client, date__gte = time).count() == 0:
                new_promo = PromotionsCustomers(IdClient = t.client, date = time, reduction = 50)
                new_promo.save()
            elif tk > 5 and PromotionsCustomers.objects.filter(IdClient = t.client, date__gte = time).count() == 0:
                new_promo = PromotionsCustomers(IdClient = t.client, date = time, reduction = 25)
                new_promo.save()
            elif  tk > 1 and PromotionsCustomers.objects.filter(IdClient = t.client, date__gte = time).count() == 0:
                print("lolo")
                new_promo = PromotionsCustomers(IdClient = t.client, date = time, reduction = 15)
                new_promo.save()
        else:
            if tk > 10 and PromotionsCustomers.objects.filter(IdClient = t.client, date__gte = time).count() == 0:
                new_promo = PromotionsCustomers(IdClient = t.client, date = time, reduction = 50)
                new_promo.save()
            elif tk > 5 and PromotionsCustomers.objects.filter(IdClient = t.client, date__gte = time).count() == 0:
                new_promo = PromotionsCustomers(IdClient = t.client, date = time, reduction = 25)
                new_promo.save()
            elif  tk > 1 and PromotionsCustomers.objects.filter(IdClient = t.client, date__gte = time).count() == 0:
                print("lala")
                new_promo = PromotionsCustomers(IdClient = t.client, date = time, reduction = 15)
                new_promo.save()
        loop += 1

    return render(request, 'home.html')