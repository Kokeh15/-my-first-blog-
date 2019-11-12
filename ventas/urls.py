from django.urls import path
from . import views

#from django.contrib.auth import login

urlpatterns = [
    path('',views.index,name='index'),
    path('contacto', views.contacto,name='contacto'),
    path ('registro',views.registro , name = 'registrarse'),
    path ('desayuno',views.desayuno , name = 'desayuno'),
    path ('almuerzo',views.almuerzo , name = 'almuerzo'),
    path ('cena', views.cena , name = 'cena')
]

