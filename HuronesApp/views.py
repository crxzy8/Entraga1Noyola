from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, context, loader
from .forms import *
from .models import *

def inicio(request):
    return render(request, 'HuronesApp/index.html')

def buscar(request):
    Huron=request.GET['nombre']
    name=hurones.objects.filter(nombre=Huron)
    return render(request, 'HuronesApp/resultados.html' , {"nombre":name})

def buscaHuron(request):
    return render(request, 'HuronesApp/buscaHuron.html')

def Hurones(request):
    if request.method == 'POST':
        form=formsHuron(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            name=info["nombre"]
            age=info["edad"]
            race=info["raza"]
            huron=hurones(nombre=name, edad=age, raza=race)
            huron.save()
            return render(request, 'HuronesApp/hurones.html', {'mensaje':"Huron Agregado"})
    else:
        form=formsHuron()
        return render(request, 'HuronesApp/hurones.html', {'form':form})

def Comida(request):
    if request.method == 'POST':
        form=formsComida(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            type=info["tipo"]
            prote=info["proteinas"]
            food=comida(tipo=type, proteinas=prote)
            food.save()
            return render(request, 'HuronesApp/comida.html', {'mensaje':"Comida Agregado"})
    else:
        form=formsComida()
        return render(request, 'HuronesApp/comida.html', {'form':form})

def Accesorios(request):
    if request.method == 'POST':
        form=formsAccessory(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            type=info["tipo"]
            price=info["precio"]
            colors=info["colores"]
            accesorios=accesorio(tipo=type,precio=price,colores=colors)
            accesorios.save()
            return render(request, 'HuronesApp/accesorios.html', {'mensaje':"Accesorio Agregado"})
    else:
        form=formsAccessory()
        return render(request, 'HuronesApp/accesorios.html', {'form':form})