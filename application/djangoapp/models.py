from django.db import models

class Promotions(models.Model):
    isFlat = models.BooleanField()
    flat = models.FloatField()
    percent = models.FloatField()
    productId = models.PositiveIntegerField()

    def __str__(self):
        return 'Promotions product: {}'.format(self.productId)

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


class Users(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class Customers(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    fidelityPoint = models.IntegerField(default=0)
    payment = models.IntegerField(default=0)
    account = models.CharField(max_length=10, default="")

class Products(models.Model):
    codeProduit = models.CharField(max_length=200)
    familleProduit = models.CharField(max_length=200)
    descriptionProduit = models.CharField(max_length=200)
    quantiteMin = models.PositiveIntegerField()
    packaging = models.PositiveIntegerField()
    prix = models.PositiveIntegerField()