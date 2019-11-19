import os

from django.apps import AppConfig
from apipkg import api_manager as api
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta

myappurl = "http://localhost:" + os.environ["WEBSERVER_PORT"]

class ApplicationConfig(AppConfig):
    name = 'application.djangoapp'

    @csrf_exempt
    def ready(self):
        # if os.environ.get('RUN_MAIN'):
        #     api.unregister(os.environ['DJANGO_APP_NAME'])
        #     api.register(myappurl, os.environ['DJANGO_APP_NAME'])
        #     clock_time = api.send_request('scheduler', 'clock/time')
        #     time = datetime.strptime(clock_time, '"%d/%m/%Y-%H:%M:%S"')
        #     time = time + timedelta(minutes=10)
        #     # Refreshes Customers
        #     api.schedule_task("gestion-promotion", "admin/crm/loadcrm", time, "day", {}, "gestion-promotion", "Promo: Update CRM")

        #     # Refreshes Products
        #     api.schedule_task("gestion-promotion", "admin/product/loadproduct", time, "day", {}, "gestion-promotion", "Promo: Update product")

        #     # Refreshes Tickets everydays
        #     api.schedule_task("gestion-promotion", "admin/tickets/loadtickets", time, "day", {}, "gestion-promotion", "Promo: Update tickets")

        #     # Refreshes Promotions for Ecommerce everydays
        #     api.schedule_task("gestion-promotion", "promo/ecommerce/calc", time, "day", {}, "gestion-promotion", "Promo: ecommerce promo")

        #     # Refreshes Promotions for Magasin everydays
        #     api.schedule_task("gestion-promotion", "promo/magasin/calc", time, "day", {}, "gestion-promotion", "Promo: magasin promo")
            
        #     # Refreshes Promotions for targeted customers everydays
        #     api.schedule_task("gestion-promotion", "promo/customers/calc", time, "day", {}, "gestion-promotion", "Promo: customers promo")
            
        #     # Refreshes Promotions for targeted customers products everydays
        #     api.schedule_task("gestion-promotion", "promo/customersproducts/calc", time, "week", {}, "gestion-promotion", "Promo: customers products promo")
        print("lol")