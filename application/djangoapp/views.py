from django.http import HttpResponse
from django.http import JsonResponse
from apipkg import api_manager as api

from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import redirect
from django.shortcuts import render
from datetime import datetime, date
from django.core import serializers

import requests
import json

from application.djangoapp.forms import *
from application.djangoapp.models import *

from application.djangoapp.controller import promotions as promotions


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
    # Refreshes Customers
    schedule_task("gestion-promotion", "admin/crm/loadcrm", datetime(year = 2019, month = 1, day = 7, hour = 1, minute = 20), "none", {}, "gestion-promotion", "loadcrm")

    # Refreshes Products
    schedule_task("gestion-promotion", "admin/product/loadproduct", datetime(year = 2019, month = 1, day = 7, hour = 1, minute = 20), "none", {}, "gestion-promotion", "loadproduct")

    return render(request, 'home.html')

# Dispatcher of promotion resources
@csrf_exempt
def promo(request):
    if request.method == 'GET':
        return promotions.index(request)
    if request.method == 'POST':
        return promotions.create(request)
    if request.method == 'DELETE':
        return promotions.destroy(request)
    if request.method == 'PATCH':
        return promotions.update(request)
    return HttpResponse("The request has been failed")

# PATCH request
def patch_request(host, url, body):
    print(" [x] Trying to send patch request to host %r " % host)
    headers = {'Host': host}
    r = requests.patch(api_services_url + url, headers=headers, data=body)
    if r.status_code == 200:
        print(" [x] Patch request successfully sent to host %r " % host)
    else:
        print(" [x] Patch request FAILED exited with error code: " % r.status_code)
    return r.status_code


# DELETE request
def delete_request(host, url, body):
    print(" [x] Trying to send delete request to host %r " % host)
    headers = {'Host': host}
    r = requests.delete(api_services_url + url, headers=headers, data=body)
    if r.status_code == 200:
        print(" [x] Delete request successfully sent to host %r " % host)
    else:
        print(" [x] Delete request FAILED exited with error code: " % r.status_code)
    return r.status_code



# All of the functions above are used to display front & interact with crm & catalogue-produit


def clear(request):
    Promotions.objects.all().delete()
    Products.objects.all().delete()
    Customers.objects.all().delete()
    return render(request, 'home.html')

# Login form
def login(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            count = Users.objects.filter(email=request.POST['email'], password=request.POST['password']).count()
            if count:
                return redirect('home')
    else:
        form = UserForm()
    return render(request, 'login.html', {'form': form})

# Home page
def home(request):
    return render(request, 'home.html')


# for Promo App
# Display all promotions
def index(request):
    if request.method == 'GET':
        data = Promotions.objects.all()
        d = { 
            "list_promo": data
        }
        return render(request, 'index.html', d)

# Function to create a promotion
def create(request):
    if request.method == 'POST':
        form = PromotionForm(request.POST)
        if form.is_valid():
            iF = form.cleaned_data['isFlat']
            f = form.cleaned_data['flat']
            per = form.cleaned_data['percent']
            pId = form.cleaned_data['productId']
            p = Promotions(isFlat=iF, flat=f, percent=per, productId=pId)
            p.save()
            form = PromotionForm()
            return render(request, 'create.html', {'form': form})

# Form to create a promotion
def displayCreate(request):
    form = PromotionForm()
    return render(request, 'create.html', {'form': form})

# Function to update a promotion
def update(request):
    if request.method == 'POST':
        form = PromotionIdForm(request.POST)
        if form.is_valid():
            idd = form.cleaned_data['id']
            iF = form.cleaned_data['isFlat']
            f = form.cleaned_data['flat']
            per = form.cleaned_data['percent']
            pId = form.cleaned_data['productId']
            Promotions.objects.filter(id=idd).update(isFlat=iF, flat=f, percent=per, productId=pId)
            form = PromotionIdForm()
            return render(request, 'update.html', {'form': form})

# Form to update a promotion
def displayUpdate(request):
    form = PromotionIdForm()
    return render(request, 'update.html', {'form': form})

# Function to delete a promotion
def delete(request):
    if request.method == 'POST':
        form = PromotionIdForm(request.POST)
        if form.is_valid():
            idd = form.cleaned_data['id']
            Promotions.objects.filter(id=idd).delete()
            form = PromotionIdForm()
            return render(request, 'delete.html', {'form': form})

# Form to delete a promotion
def displayDelete(request):
    form = PromotionIdForm()
    return render(request, 'delete.html', {'form': form})

# for Crm App
# Display all customers
def indexcrm(request):
    data = Customers.objects.all()
    d = { 
            "list_customers": data
        }
    return render(request, 'index_crm.html', d)


# Function to create a customer
@csrf_exempt
def loadcrm(request):
    if request.method == 'POST' or request.method == 'GET':
        customers = api.send_request('crm', 'api/data')
        result_expected = serializers.serialize("json", Customers.objects.all())
        crm, promo = json.dumps(customers, sort_keys=True), json.dumps(result_expected, sort_keys=True)
        if crm != promo:
            Customers.objects.all().delete()
            customers = json.loads(customers)
            for c in customers:
                record = Customers(id = c['id'], firstName = c['firstName'], lastName = c['lastName'], fidelityPoint = c['fidelityPoint'], payment = c['payment'], account = c['account'])
                record.save()
    return render(request, 'home.html')


# for Catalogue-Produit app
# Display all products
def indexproduct(request):
    data = Products.objects.all()
    d = { 
            "list_products": data
        }
    return render(request, 'index_product.html', d)

# Function to create a product
@csrf_exempt
def loadproduct(request):
    if request.method == 'POST' or request.method == 'GET':
        products = api.send_request('catalogue-produit', 'api/data')
        result_expected = serializers.serialize("json", Products.objects.all())
        prod, promo = json.dumps(products, sort_keys=True), json.dumps(result_expected, sort_keys=True)
        if prod != promo:
            Products.objects.all().delete()
            p = json.loads(products)
            for c in p['produits']:
                record = Products(id = c['id'], codeProduit = c['codeProduit'], familleProduit = c['familleProduit'], descriptionProduit = c['descriptionProduit'], quantiteMin = c['quantiteMin'], packaging = c['packaging'], prix = c['prix'])
                record.save()
    return render(request, 'home.html')
