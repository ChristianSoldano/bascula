import json
import datetime
from django.shortcuts import render, redirect
from django.http import *
from bascula.models import *
from django.contrib.auth import logout
from django.db import connection

def login(request):
    return render(request, "login.html")

def home(request):
    generadores = Generador.objects.all().filter(activo=1)
    transportistas = Transportista.objects.all().order_by('codigo').filter(activo=1)
    destinos = Destino.objects.all().order_by('nombre').filter(activo=1)
    return render(request, "home.html",
                  {'generadores': generadores,
                   'transportistas': transportistas,
                   'destinos': destinos
                   })

def pesajes(request):
    if request.user.is_superuser:
        cursor = connection.cursor()
        cursor.execute("SELECT MIN(FCREACION) FROM pesajes")
        row = cursor.fetchone()
        minDate = row[0]
        now = datetime.datetime.now()

        if minDate == None:
            return render(request, "historial.html", {'pesaje':[]})
        
        if request.method == 'GET':
            if "periodo" in request.GET:                
                try:
                    fechas = request.GET["periodo"].split(" - ")
                    desde = datetime.datetime.strptime(fechas[0], '%d/%m/%Y')
                    hasta = datetime.datetime.strptime(fechas[1], '%d/%m/%Y')
                    pesajes = Pesaje.objects.all().filter(activo=1, fcreacion__range=[desde.strftime('%Y-%m-%d %H:%M'), (hasta+ datetime.timedelta(1)).strftime('%Y-%m-%d %H:%M')]).order_by('-fcreacion')
                    return render(request, "historial.html", {'pesaje': pesajes, 'desde': desde.strftime('%d/%m/%Y'), 'hasta': hasta.strftime('%d/%m/%Y')})
                except Exception as e:  
                    pass
        hasta = (now + datetime.timedelta(1))
        pesajes = Pesaje.objects.all().filter(activo=1, fcreacion__range=[minDate, hasta.strftime('%Y-%m-%d %H:%M')]).order_by('-fcreacion')
        return render(request, "historial.html", {'pesaje': pesajes, 'desde': minDate.strftime('%d/%m/%Y'), 'hasta': hasta.strftime('%d/%m/%Y')})
    else:
         return redirect("login")

        
def GetResiduosbyIdGenerador(request):
    if request.method == 'GET':
        if "idGenerador" in request.GET:
            generador = Generador.objects.filter(id=request.GET["idGenerador"])
            if generador.exists():
                residuos = []
                for r in generador.first().residuos.filter(activo=1):
                    residuos.append(r.toJson())

                residuos.sort(key=lambda x: x["nombre"])
                return HttpResponse(json.dumps(residuos), content_type='application/json')
            else:
                return HttpResponseNotFound()
    else:
        return HttpResponseNotFound()


def GetCamionbyIdTransportista(request):
    if request.method == 'GET':
        if "idTransportista" in request.GET:
            ids = Camion.objects.filter(activo=1,
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

            pesaje = Pesaje(
                generador=generador.first().nombre,
                residuo=residuo.first().nombre,
                transportista=transportista.first().nombre,
                camion=camion.first().patente,
                destino=destino.first().nombre,
                pesaje=float(peso) - camion.first().tara,
                costo=((float(peso) - camion.first().tara)
                       * residuo.first().costo_tonelada),
                usuario=Usuario.objects.get(id=request.user.id)
            )
            pesaje.save()
            response = pesaje.toJson()
            response['usuario'] = pesaje.usuario.username
            return HttpResponse(json.dumps(response), content_type='application/json', status=200)
        else:
            return HttpResponseBadRequest()

def cambiarPassword(request):
    if request.method == 'POST':     
        if request.POST["currentPassword"] != "" and request.POST["newPassword"] != "" and request.POST["newPasswordConfirm"] != "":            
            u = request.user
            if not u.check_password(request.POST["currentPassword"]):
                return HttpResponse(json.dumps({"message": "Contraseña incorrecta"}), content_type='application/json', status=400)
            if request.POST["newPassword"] != request.POST["newPasswordConfirm"]:
                return HttpResponse(json.dumps({"message": "La nueva contraseña no coincide con la confirmación"}), content_type='application/json', status=400)
            u.set_password(request.POST["newPassword"])
            u.save()
            return HttpResponse(json.dumps({"message": "Contraseña actualizada"}), content_type='application/json', status=200)
        else:
            return HttpResponse(json.dumps({"message": "Complete todos los campos"}), content_type='application/json', status=400)
    else:
        return HttpResponse(json.dumps({"message": "Error al actualizar la contraseña"}), content_type='application/json', status=400)


def logout_request(request):
    logout(request)
    return redirect("login")


