from application.djangoapp.models import *
from django.core import serializers
from django.http import HttpResponse
from django.forms.models import modelform_factory
import json

from django.views.decorators.csrf import csrf_exempt


# PromotionsMag - Index
# Display a listing of the resource.
def index(request): 
    promo = PromotionsMag.objects.all()
    json = list(promo)
    return JsonResponse({"promo" : json})