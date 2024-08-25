# urls.py
from django.urls import path
from . import views


app_name = 'inventory'

urlpatterns = [
    path('sneaker/<int:sneaker_id>/', views.sneaker_detail, name='sneaker_detail'),
    #path('sneaker_count/', views.get_sneaker_count, name='sneaker_count'),

]