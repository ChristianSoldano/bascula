from django.shortcuts import render
from django.http import *
from bascula.models import *
import json

def login(request):
    return render(request, "login.html")

def home(request):
    generadores = Generador.objects.all()
    residuos = Residuo.objects.all().order_by('nombre')
    transportistas = Transportista.objects.all().order_by('codigo')
    camiones = Camion.objects.all().order_by('patente')
    destinos = Destino.objects.all().order_by('nombre')
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
                   'pesaje': pesajes
                   })

def GetResiduosbyIdGenerador(request):
    if request.method == 'GET':
        if "idGenerador" in request.GET:           
            ids = GeneradoresResiduos.objects.filter(generador = request.GET["idGenerador"])
            residuos = []
            for item in ids:
                r = Residuo.objects.get(id = item.residuo.id)
                residuos.append(r.toJson())
            residuos.sort(key = lambda x:x["nombre"])
            return HttpResponse(json.dumps(residuos), content_type='application/json')
    else:
        return HttpResponseNotFound()

def GetCamionbyIdTransportista(request):
    if request.method == 'GET':
        if "idTransportista" in request.GET:
            ids = Camion.objects.filter(transportista=request.GET["idTransportista"]).order_by('patente')
            camiones = []
            for item in ids:
                camiones.append(item.toJson())
            return HttpResponse(json.dumps(camiones), content_type='application/json')
    else:
        return HttpResponseNotFound()

def getTara(request):
    if request.method == 'GET':
        if "idCamion" in request.GET:
            camion = Camion.objects.get(id=request.GET["idCamion"])
        return HttpResponse(json.dumps({'tara': camion.tara}), content_type='application/json')
    else:
        return HttpResponseNotFound()

def GuardarPesaje(request):
    if request.method == 'POST':
        if "generador" and "residuo" and "transportista" and "camion" and "destino" and "peso" in request.POST:
            generador = Generador.objects.filter(id=request.POST['generador'])
            residuo = Residuo.objects.filter(id=request.POST['residuo'])
            transportista = Transportista.objects.filter(codigo=request.POST['transportista'])
            camion = Camion.objects.filter(id=request.POST['camion'])
            destino = Destino.objects.filter(id=request.POST['destino'])
            peso = request.POST['peso']
            print(request.POST['transportista']) 
            if not generador.exists() or not residuo.exists() or not transportista.exists() or not camion.exists() or not destino.exists():
                return HttpResponseBadRequest()     
                    
            Pesaje(
                generador = generador.first().nombre,
                residuo = residuo.first().nombre,
                transportista = transportista.first().nombre,
                camion = camion.first().patente,
                destino = destino.first().nombre,
                pesaje = peso,
                costo = ((float(peso) - camion.first().tara) * residuo.first().costo_tonelada),
                id_usuario = 1 #TODO CAMBIAR POR IDUSUARIO FK
            ).save()
            return HttpResponse(status=200)
        else:
            return HttpResponseBadRequest()

def tablahistorial(request):
    ids = Pesaje.objects.filter(activo=1).order_by('id')
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

def testing(request):
    generador = Generador.objects.filter(id=1)
    if not generador.exists():
        return HttpResponse("NO EXISTE")
    else:
        return HttpResponse("EXISTE")
