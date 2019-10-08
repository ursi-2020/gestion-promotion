from django import forms

class PromotionEcoForm(forms.Form):
    codeProduit = forms.CharField(max_length=200)
    familleProduit = forms.CharField(max_length=200)
    descriptionProduit = forms.CharField(max_length=200)
    quantiteMin = forms.IntegerField(min_value = 0)
    packaging = forms.IntegerField(min_value = 0)
    prix = forms.IntegerField(min_value = 0)

class PromotionIdForm(forms.Form):
    id = forms.IntegerField(min_value=1, required=True, initial=1)
    isFlat = forms.BooleanField(required=False)
    flat = forms.FloatField(required=False, initial=0)
    percent = forms.FloatField(required=False, initial=0)
    productId = forms.IntegerField(min_value=1, required=False, initial=1)

class CustomerForm(forms.Form):
    IdClient = forms.TextField(default="")
    Nom = forms.CharField(max_length=200)
    Prenom = forms.CharField(max_length=200)
    Credit = forms.DecimalField(default=0, max_digits=6, decimal_places=2)
    Paiement = forms.IntegerField(default=0)
    Compte = forms.CharField(max_length=10, default="")

class Products(forms.Form):
    codeProduit = forms.CharField(max_length=200)
    familleProduit = forms.CharField(max_length=200)
    descriptionProduit = forms.CharField(max_length=200)
    quantiteMin = forms.IntegerField(min_value = 0)
    packaging = forms.IntegerField(min_value = 0)
    prix = forms.IntegerField(min_value = 0)
    exclusivite = forms.CharField(max_length=200, default="")

class ProductsEco(forms.Form):
    codeProduit = forms.CharField(max_length=200)
    familleProduit = forms.CharField(max_length=200)
    descriptionProduit = forms.CharField(max_length=200)
    quantiteMin = forms.IntegerField(min_value = 0)
    packaging = forms.IntegerField(min_value = 0)
    prix = forms.IntegerField(min_value = 0)

class ProductsMag(forms.Form):
    codeProduit = forms.CharField(max_length=200)
    familleProduit = forms.CharField(max_length=200)
    descriptionProduit = forms.CharField(max_length=200)
    quantiteMin = forms.IntegerField(min_value = 0)
    packaging = forms.IntegerField(min_value = 0)
    prix = forms.IntegerField(min_value = 0)