from django.shortcuts import render
from django.http import *
from bascula.models import *
import json

def login(request):
    return render(request, "login.html")

def home(request):
    generadores = Generador.objects.all()
    residuos = Residuo.objects.all().order_by('residuo')
    transportistas = Transportista.objects.all().order_by('codigo')
    camiones = Camion.objects.all().order_by('patente')
    destinos = Destino.objects.all().order_by('destino')

    return render(request, "home.html",
        {'generadores': generadores, 
        'residuos': residuos, 
        'transportistas': transportistas,
        'camiones': camiones,
        'destinos': destinos
        })

def historial(request):
    generadores = Generador.objects.all()
    residuos = Residuo.objects.all().order_by('residuo')
    transportistas = Transportista.objects.all().order_by('codigo')
    camiones = Camion.objects.all().order_by('patente')
    destinos = Destino.objects.all().order_by('destino')
    pesajes = Pesaje.objects.all().order_by('-id')
    return render(request, "historial.html",
        {'generadores': generadores, 
        'residuos': residuos, 
        'transportistas': transportistas,
        'camiones': camiones,
        'destinos': destinos,
        'pesaje':pesajes
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

def GetVehiculobyIdTransportista(request):
    if request.method == 'POST':
        if "idTransportista" in request.POST:
            ids = Camion.objects.filter(id_transportista = request.POST["idTransportista"]).order_by('patente')
            camiones = []
            for item in ids:
                camiones.append({'id': item.id, 'patente': item.patente})
            return HttpResponse(json.dumps(camiones), content_type='application/json')
    else:
        return HttpResponseBadRequest()

def FijarTara(request):
    if request.method == 'POST':
        if "idPatente" in request.POST:
            ids = Camion.objects.get(id = request.POST["idPatente"])
        return HttpResponse(json.dumps(ids.tara), content_type='application/json')
    else:
        return HttpResponseBadRequest()

def GuardarPesaje(request):
    if request.method == 'POST':
        if "generador" and "residuos" and "transportista" and "camiones" and "destino" and "peso" and "tara" in request.POST:
            P = Pesaje(
                    id_generador=request.POST['generador'],
                    id_residuo=request.POST['residuos'],
                    nombre_residuo=Residuo.objects.get(id=request.POST['residuos']),
                    nombre_generador= Generador.objects.get(id=request.POST['generador']),
                    id_transportista=request.POST['transportista'],
                    nombre_transportista="FALTA ESTO",
                    id_camion=request.POST['camiones'],
                    patente_camion = Camion.objects.get(id=request.POST['camiones']),
                    id_destino=request.POST['destino'],
                    destino = Destino.objects.get(id=request.POST['destino']),  
                    id_usuario=1,
                    pesaje=request.POST["peso"],  
                    # costo= "(peso - tara) * costo del residuo",   
                    costo = 2,
                    activo=1)
            P.save()
        return print(P.id)
def tablahistorial(request):
            ids = Pesaje.objects.filter(activo = 1).order_by('id')
            pesajes = []
            for item in ids:
                pesajes.append({'id': item.id, 
                'generador': item.id_generador,
                'residuo': item.id_residuo,
                'transportista': item.id_transportista,
                'camion': item.id_camion,
                'destino': item.id_destino,
                'pesaje': item.pesaje,
                'fecha': item.f_creacion,
                'usuario': item.id_usuario})
            return HttpResponse(json.dumps(pesajes), content_type='application/json') 
    
        