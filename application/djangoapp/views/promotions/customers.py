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
    PromotionsCustomers.objects.all().delete()
    tickets = Tickets.objects.all()
    loop = 1
    for t in tickets:
        tk = Tickets.objects.filter(client = t.client).count()
        if loop == 1:
            if tk > 10 and Tickets.objects.all()[:loop].filter(client = t.client).count() == 0:
                new_promo = PromotionsCustomers(IdClient = t.client, reduction = 50)
                new_promo.save()
            elif tk > 5 and Tickets.objects.all()[:loop].filter(client = t.client).count() == 0:
                new_promo = PromotionsCustomers(IdClient = t.client, reduction = 25)
                new_promo.save()
            elif  tk > 3 and Tickets.objects.all()[:loop].filter(client = t.client).count() == 0:
                new_promo = PromotionsCustomers(IdClient = t.client, reduction = 15)
                new_promo.save()
        else:
            if tk > 10 and Tickets.objects.all()[:loop].filter(client = t.client).count() == 0:
                new_promo = PromotionsCustomers(IdClient = t.client, reduction = 50)
                new_promo.save()
            elif tk > 5 and Tickets.objects.all()[:loop].filter(client = t.client).count() == 0:
                new_promo = PromotionsCustomers(IdClient = t.client, reduction = 25)
                new_promo.save()
            elif  tk > 3 and Tickets.objects.all()[:loop].filter(client = t.client).count() == 0:
                new_promo = PromotionsCustomers(IdClient = t.client, reduction = 15)
                new_promo.save()
        loop += 1
    # # it's a try
    # cu = Customers.objects.filter(Nom='Sarkozy-51')
    # for c in cu:
    #     if c.Nom == 'Sarkozy-51':
    #         print('ouiii')
    #     new_promo = PromotionsCustomers(id = c['id'], IdClient = c['IdClient'], Nom = c['Nom'], Prenom = c['Prenom'], Credit = c['Credit'], Paiement = c['Paiement'], NbRefus = c['NbRefus'], Arembourser = c['Arembourser'], Compte = c['Compte'], Age = c['Age'], Sexe = c['Sexe'], Email = c['Email'], carteFid=c['carteFid'], reduction = 50)
    #     new_promo.save()
    return render(request, 'home.html')