from django.http import HttpResponse
from django.http import JsonResponse
from apipkg import api_manager as api

from application.djangoapp.models import *

from django.shortcuts import redirect
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json

# for Crm App
# Display all customers
def indexcrm(request):
    data = Customers.objects.all()
    d = { 
            "list_customers": data
        }
    return render(request, 'index_crm.html', d)


# Function to create a customer
@csrf_exempt
def loadcrm(request):
    if request.method == 'POST' or request.method == 'GET':
        customers = api.send_request('crm', 'api/data')
        result_expected = serializers.serialize("json", Customers.objects.all())
        crm, promo = json.dumps(customers, sort_keys=True), json.dumps(result_expected, sort_keys=True)
        if crm != promo:
            Customers.objects.all().delete()
            customers = json.loads(customers)
            for c in customers:
                record = Customers(id = c['id'], IdClient = c['IdClient'], Nom = c['Nom'], Prenom = c['Prenom'], Credit = c['Credit'], Paiement = c['Paiement'], Compte = c['Compte'], carteFid=c['carteFid'])
                record.save()
    return render(request, 'home.html')