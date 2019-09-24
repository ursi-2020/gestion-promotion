from application.djangoapp.models import *
from django.core import serializers
from django.http import HttpResponse
from django.forms.models import modelform_factory
import json


from django.views.decorators.csrf import csrf_exempt


# Promotions - Index
# Display a listing of the resource.
def index(request):
    data = serializers.serialize("json", Promotions.objects.all())
    return HttpResponse(json.dumps(data),content_type='application/json')

# Promotions - Create
# Store a newly created resource in database.
def create(request):
    p = Promotions(isFlat = request.POST['isFlat'], flat = request.POST['flat'], percent = request.POST['percent'], productId = request.POST['productId'])
    p.save()
    return HttpResponse("Successfully created")

# Promotions - Update
# Update the specified resource in database.
def update(request):
    patch_params = QueryDict(request.body)
    Promotions.objects.filter(id=patch_params.get("id")).update(isFlat=patch_params.get('isFlat'), flat=patch_params.get('flat'), percent=patch_params.get('percent'), productId=patch_params.get('productId'))
    return HttpResponse("succesfully updated")

# Promotions - Destroy
# Remove the specified resource from database.
def destroy(request):
    delete_params = QueryDict(request.body).get("id")
    Promotions.objects.filter(id=delete_params).delete()
    return HttpResponse("succesfully destroyed")