
from django.shortcuts import render, redirect
from django.http import HttpResponse
from ventas.models import Producto



# Create your views here.

def index(request):
    return render(request,'StartVegan.html',{})



def contacto(request):
    return render(request,'Contacto.html' ,{})
    


def registro(request):
    return render(request,'registrarse.html',{}) 
    
    
    
def desayuno(request):
    return render(request,'Desayuno.html',{}) 
    
    
def almuerzo(request):
    return render(request,'Almuerzo.html',{}) 
    
    
def cena(request):
    return render(request,'Cena.html',{}) 