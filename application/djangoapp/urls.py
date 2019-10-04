from django.urls import path

from application.djangoapp.views import customers as c
from application.djangoapp.views import ecommerce as e
from application.djangoapp.views import magasin as m
from application.djangoapp.views import products as p
from application.djangoapp.views import scheduler as s
from application.djangoapp.views import tools as t


urlpatterns = [

    # Public routes

    # Promotions Ecommerce
    path('promo/ecommerce', e.promoEco, name='promoEco'),

    # Promotions Magasin
    path('promo/magasin', m.promoMag, name='promoMag'),

    # Private routes

    # Calculte promotions Ecommerce
    path('promo/ecommerce/calc', e.calcPromoEco, name='calcPromoEco'),

    #Calculate promotions Magasin
    path('promo/magasin/calc', m.calcPromoMag, name='calcPromoMag'),

    # Display promotions
    path('promo/magasin/indexpromomag', m.indexpromomag, name='indexpromomag'),
    path('promo/ecommerce/indexpromoeco', e.indexpromoeco, name='indexpromoeco'),


    # Clear all datas from databases
    path('admin/clear', t.clear, name="clear"),

	# Home page
    path('admin/home', t.home, name='home'),

    # Requests in front page to crm
    path('admin/crm/indexcrm', c.indexcrm, name='indexcrm'),
    path('admin/crm/loadcrm', c.loadcrm, name='loadcrm'),

    # Requests in front page to catalogue produit
    path('admin/product/indexproduct', p.indexproduct, name='indexproduct'),
    path('admin/product/indexproducteco', p.indexproducteco, name='indexproducteco'),
    path('admin/product/indexproductmag', p.indexproductmag, name='indexproductmag'),
    path('admin/product/loadproduct', p.loadproduct, name='loadproduct'),

    # Refresh all the databases by the scheduler
    path('admin/refresh', s.refresh, name="refresh")


]