from django.shortcuts import render
from django.http import HttpResponse
from bascula.models import *

def home(request):
    generadores = Generador.objects.all()
    residuos = Residuo.objects.all()
    transportistas = Transportista.objects.all()
    camiones = Camion.objects.all()
    destinos = Destino.objects.all()

    return render(request, 'home.html',
        {'generadores': generadores, 
        'residuos': residuos, 
        'transportistas': transportistas,
        'camiones': camiones,
        'destinos': destinos
        })
