from django.http import HttpResponse
from django.http import JsonResponse
from apipkg import api_manager as api

from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from application.djangoapp.models import *

from django.views.decorators.csrf import csrf_exempt
from application.djangoapp.controller import promotions as promotions

import json

# def index(request):
#     time = api.send_request('scheduler', 'clock/time')
#     return HttpResponse("L'heure de la clock est %r" % time)

@csrf_exempt
def promo(request):
    if request.method == 'GET':
        return promotions.index(request)
    if request.method == 'POST':
        return promotions.create(request)
    return HttpResponse("VOILA VOILA")

# GET request from crm
get = api.send_request('crm', 'customer')
print(HttpResponse(json.dumps(get), content_type='application/json'))