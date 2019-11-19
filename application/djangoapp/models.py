from django.db import models
from datetime import datetime, timedelta

class Article(models.Model):
    nom = models.CharField(max_length=200)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return 'Article: {}'.format(self.nom)


class Vente(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return 'Vente: {} - {}'.format(self.article.nom, self.date)


# # # All models for handling promotions in this app

# contains all promotions for ecommerce
class PromotionsEco(models.Model):
    codeProduit = models.CharField(max_length=200)
    familleProduit = models.CharField(max_length=200)
    descriptionProduit = models.CharField(max_length=200)
    quantiteMin = models.PositiveIntegerField()
    packaging = models.PositiveIntegerField()
    prix = models.PositiveIntegerField()
    prixOriginel = models.PositiveIntegerField(default=0)
    reduction = models.PositiveIntegerField(default=0)

# contains all promotions for magasin
class PromotionsMag(models.Model):
    codeProduit = models.CharField(max_length=200)
    familleProduit = models.CharField(max_length=200)
    descriptionProduit = models.CharField(max_length=200)
    quantiteMin = models.PositiveIntegerField()
    packaging = models.PositiveIntegerField()
    prix = models.PositiveIntegerField()
    prixOriginel = models.PositiveIntegerField(default=0)
    reduction = models.PositiveIntegerField(default=0)

# contains all promotions targeted to customers
class PromotionsCustomers(models.Model):    
    IdClient = models.TextField(blank=False)
    date = models.DateField()
    reduction = models.IntegerField(default=0)

class PromotionsCustomersProducts(models.Model):
    date = models.DateField()
    IdClient = models.TextField(blank=False)
    codeProduit = models.CharField(max_length=20)
    quantity = models.IntegerField(default = 0)
    reduction = models.IntegerField(default = 0)

# # # All models to save all datas got from other apps

# # From CRM

# contains all customers from CRM
class Customers(models.Model):
    IdClient = models.TextField(blank=False)
    Nom = models.CharField(max_length=200)
    Prenom = models.CharField(max_length=200)
    Credit = models.IntegerField(default=0)
    Paiement = models.IntegerField()
    Compte = models.CharField(max_length=10, default="")
    carteFid = models.IntegerField()

# contains all articles in tickets.articles from crm
class ArticlesList(models.Model):
    codeProduit = models.CharField(max_length=20)
    quantity = models.IntegerField()

# contains all the tickets from crm
class Tickets(models.Model):
    date = models.DateTimeField()
    prix = models.IntegerField()
    client = models.TextField(blank=False)
    articles = models.ManyToManyField(ArticlesList)
    pointsFidelite = models.IntegerField()
    modePaiement = models.CharField(max_length=10)

# # From catalogue-produit

# contains all products from catalogue-produit
class Products(models.Model):
    codeProduit = models.CharField(max_length=200)
    familleProduit = models.CharField(max_length=200)
    descriptionProduit = models.CharField(max_length=200)
    quantiteMin = models.PositiveIntegerField()
    packaging = models.PositiveIntegerField()
    prix = models.PositiveIntegerField()
    exclusivite = models.CharField(max_length=200, default="")
    
# contains all ecommerce products from catalogue-produit
class ProductsEco(models.Model):
    codeProduit = models.CharField(max_length=200)
    familleProduit = models.CharField(max_length=200)
    descriptionProduit = models.CharField(max_length=200)
    quantiteMin = models.PositiveIntegerField()
    packaging = models.PositiveIntegerField()
    prix = models.PositiveIntegerField()


# contains all magasin products from catalogue-produit
class ProductsMag(models.Model):
    codeProduit = models.CharField(max_length=200)
    familleProduit = models.CharField(max_length=200)
    descriptionProduit = models.CharField(max_length=200)
    quantiteMin = models.PositiveIntegerField()
    packaging = models.PositiveIntegerField()
    prix = models.PositiveIntegerField()

