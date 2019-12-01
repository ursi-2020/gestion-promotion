from django.http import HttpResponse
from django.http import JsonResponse
from apipkg import api_manager as api

from application.djangoapp.models import *
import requests
import json
from django.core import serializers

from django.shortcuts import redirect
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt


# for Catalogue-Produit app
# Display all products
def indexproduct(request):
    data = Products.objects.all()
    d = { 
            "list_products": data
        }
    return render(request, 'index_product.html', d)

# Display products ecommerce
def indexproducteco(request):
    data = ProductsEco.objects.all()
    d = { 
            "list_products": data
        }
    return render(request, 'index_product_eco.html', d)

# Display products magasin
def indexproductmag(request):
    data = ProductsMag.objects.all()
    d = { 
            "list_products": data
        }
    return render(request, 'index_product_mag.html', d)

# Function to create a product
@csrf_exempt
def loadproduct(request):
    if request.method == 'POST' or request.method == 'GET':
        products = api.send_request('catalogue-produit', 'api/get-all')

        result_expected = serializers.serialize("json", Products.objects.all())
        prod, promo = json.dumps(products, sort_keys=True), json.dumps(result_expected, sort_keys=True)

        if prod != promo:
            Products.objects.all().delete()
            print(str(products))
            p = json.loads(products)
            for c in p['produits']:
                record = Products(id = c['id'], codeProduit = c['codeProduit'], familleProduit = c['familleProduit'], descriptionProduit = c['descriptionProduit'], quantiteMin = c['quantiteMin'], packaging = c['packaging'], prixFournisseur = c['prixFournisseur'], prix = c['prix'], exclusivite = c['exclusivite'])
                record.save()

    if request.method == 'POST' or request.method == 'GET':
        products = api.send_request('catalogue-produit', 'api/get-ecommerce')
        
        result_expected = serializers.serialize("json", ProductsEco.objects.all())
        prod, promo = json.dumps(products, sort_keys=True), json.dumps(result_expected, sort_keys=True)

        if prod != promo:
            ProductsEco.objects.all().delete()
            p = json.loads(products)
            for c in p['produits']:
                record = ProductsEco(id = c['id'], codeProduit = c['codeProduit'], familleProduit = c['familleProduit'], descriptionProduit = c['descriptionProduit'], quantiteMin = c['quantiteMin'], packaging = c['packaging'], prixFournisseur = c['prixFournisseur'], prix = c['prix'])
                record.save()

    if request.method == 'POST' or request.method == 'GET':
        products = api.send_request('catalogue-produit', 'api/get-magasin')
        
        result_expected = serializers.serialize("json", ProductsMag.objects.all())
        prod, promo = json.dumps(products, sort_keys=True), json.dumps(result_expected, sort_keys=True)

        if prod != promo:
            ProductsMag.objects.all().delete()
            p = json.loads(products)
            for c in p['produits']:
                record = ProductsMag(id = c['id'], codeProduit = c['codeProduit'], familleProduit = c['familleProduit'], descriptionProduit = c['descriptionProduit'], quantiteMin = c['quantiteMin'], packaging = c['packaging'], prixFournisseur = c['prixFournisseur'], prix = c['prix'])
                record.save()
    return render(request, 'home.html')