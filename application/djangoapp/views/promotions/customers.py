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
    # it's a try
    cu = Customers.objects.filter(Nom='Sarkozy-51')
    for c in cu:
        if c.Nom == 'Sarkozy-51':
            print('ouiii')
        new_promo = PromotionsCustomers(id = c['id'], IdClient = c['IdClient'], Nom = c['Nom'], Prenom = c['Prenom'], Credit = c['Credit'], Paiement = c['Paiement'], NbRefus = c['NbRefus'], Arembourser = c['Arembourser'], Compte = c['Compte'], Age = c['Age'], Sexe = c['Sexe'], Email = c['Email'], carteFid=c['carteFid'], reduction = 50)
        new_promo.save()
    return render(request, 'home.html')

api.send_request('gestion-promotion', 'promo/customers/calc')