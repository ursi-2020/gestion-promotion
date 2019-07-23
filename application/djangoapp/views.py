from django.http import HttpResponse
from apipkg import api_manager as api

from django.views.decorators.csrf import csrf_exempt
from application.djangoapp.controller import promotions as promotions

# def index(request):
#     time = api.send_request('scheduler', 'clock/time')
#     return HttpResponse("L'heure de la clock est %r" % time)


@csrf_exempt
def promo(request):
    if request.method == 'GET':
        return promotions.index(request)
    if request.method == 'POST':
        return promotions.create(request)
    return HttpResponse("The request has been failed")
