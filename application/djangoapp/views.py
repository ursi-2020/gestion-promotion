from django.http import HttpResponse
from django.http import JsonResponse
from apipkg import api_manager as api

from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import redirect
from django.shortcuts import render
from datetime import datetime, date

import requests

from application.djangoapp.forms import *
from application.djangoapp.models import *

from application.djangoapp.controller import promotions as promotions

time = api.send_request('scheduler', 'clock/time')
print("time = "+str(time))


def schedule_task(host, url, time, recurrence, data, source, name):
    time_str = time.strftime('%d/%m/%Y-%H:%M:%S')
    headers = {'Host': 'scheduler'}
    data = {"target_url": url, "target_app": host, "time": time_str, "recurrence": recurrence, "data": data, "source_app": source, "name": name}
    r = requests.post(api.api_services_url + 'schedule/add', headers = headers, json = data)
    print(r.status_code)
    print(r.text)
    return r.text

# api.post_request("scheduler", "/reset", body={})
schedule_task("gestion-promotion", "admin/promotions/create", datetime(year = 2019, month = 1, day = 7, hour = 10, minute = 00), "none", "none", "gestion-promotion", "create")
# api.send_request("scheduler", "/")
# api.send_request("scheduler", "/schedule/list")


# Dispatcher of promotion resources
# @csrf_exempt
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



# All of the functions above are used to display front

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
    if request.method == 'GET':
        data = api.send_request('crm', 'customer')
        d = { 
            "list_customer": data
        }
        return render(request, 'index_crm.html', d)

# Function to create a customer
def createcrm(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            fn = form.cleaned_data['firstName']
            ln = form.cleaned_data['lastName']
            fp = form.cleaned_data['fidelityPoint']
            b = {'firstName': fn, 'lastName': ln, 'fidelityPoint': fp}
            post = api.post_request('crm', 'customer/', body=b)
            form = CustomerForm()
            return render(request, 'createcrm.html', {'form': form})

# Form to create a customer
def displayCreatecrm(request):
    form = CustomerForm()
    return render(request, 'createcrm.html', {'form': form})