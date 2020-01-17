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
# Display all tickets
def indextickets(request):
    data = Tickets.objects.all()
    d = { 
            "list_tickets": data
        }
    return render(request, 'index_tickets.html', d)

# load all tickets from crm
@csrf_exempt
def loadtickets(request):
    if request.method == 'POST' or request.method == 'GET':
        tickets = api.send_request('crm', 'api/get_tickets/promo')
        
        # result_expected = serializers.serialize("json", Tickets.objects.all())
        # prod, promo = json.dumps(tickets, sort_keys=True), json.dumps(result_expected, sort_keys=True)
        # if prod != promo:
        #     Tickets.objects.all().delete()
        t = json.loads(tickets)
        for c in t['tickets']:
            record = Tickets(id = c['id'], date = c['date'], prix = c['prix'], client = c['client'], pointsFidelite = c['pointsFidelite'], modePaiement = c['modePaiement'])
            record.save()
            for a in c['articles']:
                arti = ArticlesList(codeProduit = a['codeProduit'], quantity = a['quantity'])
                arti.save()
                record.articles.add(arti)
    return render(request, 'home.html')