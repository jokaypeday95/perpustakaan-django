from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buku/', views.buku, name='buku'),
    path('penerbit/', views.penerbit, name='penerbit'),

]