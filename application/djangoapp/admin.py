from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Article)
admin.site.register(models.Vente)
admin.site.register(models.Customers)
admin.site.register(models.Products)
admin.site.register(models.ProductsEco)
admin.site.register(models.ProductsMag)
admin.site.register(models.PromotionsEco)
admin.site.register(models.PromotionsMag)
admin.site.register(models.PromotionsCustomers)
