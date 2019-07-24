from django.urls import path

from . import views

urlpatterns = [

    # Create
    path('admin/promotions/displayCreate', views.displayCreate, name='displayCreate'),
    path('admin/promotions/create', views.create, name='create'),

    # Read
    path('admin/promotions/index', views.index, name='index'),

    # Update
    path('admin/promotions/displayUpdate', views.displayUpdate, name='displayUpdate'),
    path('admin/promotions/update', views.update, name='update'),

    # Delete
    path('admin/promotions/displayDelete', views.displayDelete, name='displayDelete'),
    path('admin/promotions/delete', views.delete, name='delete'),

    # Resource dispatcher
	path('promo', views.promo, name='promo'),

	# Login form & home page
    path('login', views.login, name='login'),
    path('admin/home', views.home, name='home'),

    # Requests in front page to crm
    path('admin/crm/indexcrm', views.indexcrm, name='indexcrm'),

    path('admin/crm/displayCreatecrm', views.displayCreatecrm, name='displayCreatecrm'),
    path('admin/crm/createcrm', views.createcrm, name='createcrm'),
]