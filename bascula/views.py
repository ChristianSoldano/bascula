import json
import datetime
from django import forms 
from django.shortcuts import render, redirect
from django.http import *
from bascula.models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm


def login(request):
    return render(request, "login.html")


def home(request):
    generadores = Generador.objects.all().filter(activo=1)
    residuos = Residuo.objects.all().order_by('nombre').filter(activo=1)
    transportistas = Transportista.objects.all().order_by('codigo').filter(activo=1)
    camiones = Camion.objects.all().order_by('patente').filter(activo=1)
    destinos = Destino.objects.all().order_by('nombre').filter(activo=1)
    return render(request, "home.html",
                  {'generadores': generadores,
                   'residuos': residuos,
                   'transportistas': transportistas,
                   'camiones': camiones,
                   'destinos': destinos
                   })


def historial(request):
    generadores = Generador.objects.all().filter(activo=1)
    residuos = Residuo.objects.all().order_by('nombre').filter(activo=1)
    transportistas = Transportista.objects.all().order_by('codigo').filter(activo=1)
    camiones = Camion.objects.all().order_by('patente').filter(activo=1)
    destinos = Destino.objects.all().order_by('nombre').filter(activo=1)
    pesajes = Pesaje.objects.all().filter(activo=1).order_by('-id')
    date = datetime.datetime.now

    return render(request, "historial.html",
                  {'generadores': generadores,
                   'residuos': residuos,
                   'transportistas': transportistas,
                   'camiones': camiones,
                   'destinos': destinos,
                   'pesaje': pesajes,
                   'fecha': date
                   })


def GetResiduosbyIdGenerador(request):
    if request.method == 'GET':
        if "idGenerador" in request.GET:
            ids = GeneradoresResiduos.objects.filter(
                generador=request.GET["idGenerador"])
            residuos = []
            for item in ids:
                r = Residuo.objects.get(id=item.residuo.id)
                residuos.append(r.toJson())
            residuos.sort(key=lambda x: x["nombre"])
            return HttpResponse(json.dumps(residuos), content_type='application/json')
    else:
        return HttpResponseNotFound()


def GetCamionbyIdTransportista(request):
    if request.method == 'GET':
        if "idTransportista" in request.GET:
            ids = Camion.objects.filter(
                transportista=request.GET["idTransportista"]).order_by('patente')
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
            transportista = Transportista.objects.filter(
                codigo=request.POST['transportista'])
            camion = Camion.objects.filter(id=request.POST['camion'])
            destino = Destino.objects.filter(id=request.POST['destino'])
            peso = request.POST['peso']
            print(request.POST['transportista'])
            if not generador.exists() or not residuo.exists() or not transportista.exists() or not camion.exists() or not destino.exists():
                return HttpResponseBadRequest()

            Pesaje(
                generador=generador.first().nombre,
                residuo=residuo.first().nombre,
                transportista=transportista.first().nombre,
                camion=camion.first().patente,
                destino=destino.first().nombre,
                pesaje=peso,
                costo=((float(peso) - camion.first().tara)
                       * residuo.first().costo_tonelada),
                id_usuario=1  # TODO CAMBIAR POR IDUSUARIO FK
            ).save()
            return HttpResponse(status=200)
        else:
            return HttpResponseBadRequest()

def logout_request(request):
    logout(request)
    return redirect("login")
