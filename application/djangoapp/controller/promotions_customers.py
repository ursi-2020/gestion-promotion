from application.djangoapp.models import *
from django.core import serializers
from django.http import HttpResponse
from django.forms.models import modelform_factory
import json

from django.http import JsonResponse
from apipkg import api_manager as api

from django.views.decorators.csrf import csrf_exempt

# PromotionsCustomers - Index
# Display a listing of the resource.
def index(request):
    clock_time = api.send_request('scheduler', 'clock/time')
    time = datetime.strptime(clock_time, '"%d/%m/%Y-%H:%M:%S"')
    time = time - timedelta(weeks=1)
    promo = PromotionsCustomers.objects.filter(date__gt = time).values()
    json = list(promo)
    return JsonResponse({"promo" : json})