from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Article)
admin.site.register(models.Vente)
admin.site.register(models.Promotions)
admin.site.register(models.Users)
admin.site.register(models.Customers)
admin.site.register(models.Products)
