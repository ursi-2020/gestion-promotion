from django.http import HttpResponse
from django.http import JsonResponse
from apipkg import api_manager as api

import requests
from datetime import datetime, timedelta

from application.djangoapp.models import *

from django.shortcuts import redirect
from django.shortcuts import render

# Function to schedule tasks given by the SOC
def schedule_task(host, url, time, recurrence, data, source, name):
    time_str = time.strftime('%d/%m/%Y-%H:%M:%S')
    headers = {'Host': 'scheduler'}
    data = {"target_url": url, "target_app": host, "time": time_str, "recurrence": recurrence, "data": data, "source_app": source, "name": name}
    r = requests.post(api.api_services_url + 'schedule/add', headers = headers, json = data)
    print(r.status_code)
    print(r.text)
    return r.text


# Refreshes the two databases Products and Customers in posting to CRM and catalogue-produit to refresh all datas
def refresh(request):
    clock_time = api.send_request('scheduler', 'clock/time')
    time = datetime.strptime(clock_time, '"%d/%m/%Y-%H:%M:%S"')
    time = time + timedelta(minutes=10)
    # Refreshes Customers
    schedule_task("gestion-promotion", "admin/crm/loadcrm", time, "minute", {}, "gestion-promotion", "loadcrm")

    # Refreshes Products
    schedule_task("gestion-promotion", "admin/product/loadproduct", time, "minute", {}, "gestion-promotion", "loadproduct")

    # Refreshes Promotions for Ecommerce everydays
    schedule_task("gestion-promotion", "promo/ecommerce/calc", time, "day", {}, "gestion-promotion", "Calc ecommerce promos")

    # Refreshes Promotions for Magasin everydays
    schedule_task("gestion-promotion", "promo/magasin/calc", time, "day", {}, "gestion-promotion", "Calc magasin promos")

    return render(request, 'home.html')