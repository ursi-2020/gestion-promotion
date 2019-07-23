from django.urls import path

from . import views

urlpatterns = [
	path('promo', views.promo, name='promo'),
]