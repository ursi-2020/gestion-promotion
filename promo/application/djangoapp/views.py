from django.http import HttpResponse
from apipkg import api_manager as api
from application.djangoapp.models import *

from django.views.decorators.csrf import csrf_exempt
from application.djangoapp.controller import promotions as promotions

@csrf_exempt
def promo(request):
    if request.method == 'GET':
        return promotions.index(request)
    if request.method == 'POST':
        return promotions.create(request)
    return HttpResponse("VOILA VOILA")


