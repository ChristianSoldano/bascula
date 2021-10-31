from django.shortcuts import render
from django.http import *
from bascula.models import *
import json

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

def GetResiduosbyIdGenerador(request):
    if request.method == 'POST':
        if "idGenerador" in request.POST:
            ids = GeneradoresResiduos.objects.filter(id_generador = request.POST["idGenerador"])
            residuos = []
            for item in ids:
                r = Residuo.objects.get(id=item.id_residuo.id)
                residuos.append({'id': r.id, 'residuo': r.residuo})
            return HttpResponse(json.dumps(residuos), content_type='application/json')
    else:
        return HttpResponseBadRequest()
