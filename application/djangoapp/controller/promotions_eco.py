from application.djangoapp.models import *
from django.core import serializers
from django.http import HttpResponse
from django.forms.models import modelform_factory
import json


from django.views.decorators.csrf import csrf_exempt


# PromotionsEco - Index
# Display a listing of the resource.
def index(request):
    promo = PromotionsEco.objects.values()
    json = list(promo)
    return JsonResponse({"promo" : json})