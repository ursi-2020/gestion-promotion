from application.djangoapp.models import *
from django.core import serializers
from django.http import HttpResponse, QueryDict
from application.djangoapp.controller import promotions as promotions
from django.forms.models import modelform_factory
import json

def index(request):
    data = serializers.serialize("json", Promotions.objects.all())
    return HttpResponse(json.dumps(data),content_type='application/json')

def create(request):
    p = Promotions(isFlat = request.POST['isFlat'], flat = request.POST['flat'], percent = request.POST['percent'], productId = request.POST['productId'])
    p.save()
    return HttpResponse("succesfully created")