from django.http import HttpResponse
from django.http import JsonResponse
from apipkg import api_manager as api

import requests
from datetime import datetime, timedelta

from application.djangoapp.models import *

from django.shortcuts import redirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt



# Refreshes the two databases Products and Customers in posting to CRM and catalogue-produit to refresh all datas
@csrf_exempt
def refresh(request):
    clock_time = api.send_request('scheduler', 'clock/time')
    time = datetime.strptime(clock_time, '"%d/%m/%Y-%H:%M:%S"')
    time = time + timedelta(minutes=10)
    # Refreshes Customers
    api.schedule_task("gestion-promotion", "admin/crm/loadcrm", time, "day", {}, "gestion-promotion", "Promo: Update CRM")

    # Refreshes Products
    api.schedule_task("gestion-promotion", "admin/product/loadproduct", time, "day", {}, "gestion-promotion", "Promo: Update product")

    # Refreshes Tickets everydays
    api.schedule_task("gestion-promotion", "admin/crm/loadtickets", time, "day", {}, "gestion-promotion", "Promo: Update tickets")

    # Refreshes Promotions for Ecommerce everydays
    api.schedule_task("gestion-promotion", "promo/ecommerce/calc", time, "day", {}, "gestion-promotion", "Promo: ecommerce promo")

    # Refreshes Promotions for Magasin everydays
    api.schedule_task("gestion-promotion", "promo/magasin/calc", time, "day", {}, "gestion-promotion", "Promo: magasin promo")
    
    # Refreshes Promotions for targeted customers everydays
    api.schedule_task("gestion-promotion", "promo/customers/calc", time, "week", {}, "gestion-promotion", "Promo: customers promo")
    
    # Refreshes Promotions for targeted customers products everydays
    api.schedule_task("gestion-promotion", "promo/customersproducts/calc", time, "week", {}, "gestion-promotion", "Promo: customers products promo")
    

    return render(request, 'home.html')