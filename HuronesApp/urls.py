from django.urls import path
from HuronesApp.views import *

urlpatterns = [
    path('', inicio, name='index'),
    path('Hurones/', Hurones, name="hurones"),
    path('Comida/', Comida, name="comida"),
    path('Accesorios/', Accesorios, name="accesorios"),
    path('buscaHuron/', buscaHuron, name="buscaHuron"),
    path('buscar/', buscar, name="buscar"),
]