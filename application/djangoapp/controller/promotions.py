from application.djangoapp.models import *
from django.core import serializers
from django.http import HttpResponse
from django.forms.models import modelform_factory
import json

from django.http import JsonResponse
from apipkg import api_manager as api

from django.views.decorators.csrf import csrf_exempt


# Promotions - Index
# Display a listing of the resource.
def index(request): 
    promo = Promotions.objects.values()
    json = list(promo)
    return JsonResponse({"promo" : json})

# Promotions - Create
# Store a newly created resource in database.
def create(request):
    p = Promotions(isFlat = request.POST['isFlat'], flat = request.POST['flat'], percent = request.POST['percent'], productId = request.POST['productId'])
    if Promotions.objects.filter(productId=request.POST['productId']).count() == 0:
        p.save()
        return HttpResponse("Successfully created")
    else:
        return HttpResponse("Promotion with same productId already exists in database")

# Promotions - Update
# Update the specified resource in database.
def update(request):
    patch_params = QueryDict(request.body)
    Promotions.objects.filter(id=patch_params.get("id")).update(isFlat=patch_params.get('isFlat'), flat=patch_params.get('flat'), percent=patch_params.get('percent'), productId=patch_params.get('productId'))
    return HttpResponse("successfully updated")

# Promotions - Destroy
# Remove the specified resource from database.
def destroy(request):
    delete_params = QueryDict(request.body).get("id")
    Promotions.objects.filter(id=delete_params).delete()
    return HttpResponse("successfully destroyed")