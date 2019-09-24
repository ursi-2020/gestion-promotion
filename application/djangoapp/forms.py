from django import forms

class UserForm(forms.Form):
    email = forms.CharField(max_length=200, initial='admin')
    password = forms.CharField(max_length=200, initial='admin')

class PromotionForm(forms.Form):
    isFlat = forms.BooleanField(required=False)
    flat = forms.FloatField(required=False, initial=0)
    percent = forms.FloatField(required=False, initial=0)
    productId = forms.IntegerField(min_value=1, required=False, initial=1)

class PromotionIdForm(forms.Form):
    id = forms.IntegerField(min_value=1, required=True, initial=1)
    isFlat = forms.BooleanField(required=False)
    flat = forms.FloatField(required=False, initial=0)
    percent = forms.FloatField(required=False, initial=0)
    productId = forms.IntegerField(min_value=1, required=False, initial=1)

class CustomerForm(forms.Form):
    firstName = forms.CharField(max_length=200)
    lastName = forms.CharField(max_length=200)
    fidelityPoint = forms.IntegerField(min_value=0)