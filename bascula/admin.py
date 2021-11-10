from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from bascula import *
from bascula.models import *
    

@admin.register(Generador)
class GeneradorAdmin(admin.ModelAdmin):
    list_display = [ 'nombre', 'nombreFantasia', 'cuit']
    list_display_links = ['nombre']
    search_fields = ['nombre', 'nombre_fantasia', 'cuit']
    ordering = ['nombre']
    filter_horizontal = ('residuos',)
    list_per_page = 20

    def nombreFantasia(self, obj):
        return obj.nombre_fantasia

    nombreFantasia.short_description = 'Nombre de Fantasia'

class CamionInline(admin.TabularInline):
    model = Camion

@admin.register(Transportista)
class TransportistaAdmin(admin.ModelAdmin):
    inlines = [CamionInline,]
    list_display = [ 'codigo' ,'nombre', 'nombreFantasia', 'cuit']
    list_display_links = [ 'codigo' ,'nombre']
    search_fields = ['nombre', 'nombre_fantasia', 'cuit', 'codigo']
    ordering = ['nombre']
    list_per_page = 20

    def nombreFantasia(self, obj):
        return obj.nombre_fantasia

    nombreFantasia.short_description = 'Nombre de Fantasia'

@admin.register(Destino)
class DestinoAdmin(admin.ModelAdmin):
    list_display = [ 'nombre']
    list_display_links = [ 'nombre']
    search_fields = ['nombre']
    ordering = ['nombre']
    list_per_page = 20

    
@admin.register(Residuo)
class ResiduoAdmin(admin.ModelAdmin):
    list_display = [ 'nombre', 'costoTonelada']
    list_display_links = [ 'nombre']
    search_fields = ['nombre']
    ordering = ['nombre']
    list_per_page = 20

    def costoTonelada(self, obj):
        return "${}".format(obj.costo_tonelada)

    costoTonelada.short_description = 'Costo Tonelada'


@admin.register(Pesaje)
class PesajeAdmin(admin.ModelAdmin):
    list_display = ['getfecha', 'getUsuario', 'generador','residuo','transportista','camion','destino', 'getPesaje', 'getCosto']
    search_fields = ['fcreacion', 'usuario__username', 'generador','residuo','transportista','camion','destino']
    ordering = ['-fcreacion']
    list_per_page = 20

    def getfecha(self, obj):
        return "{}".format(obj.fcreacion.strftime('%d/%m/%Y %H:%M'))

    getfecha.short_description = 'Fecha'

    def getUsuario(self, obj):
        return obj.usuario

    getUsuario.short_description = 'Usuario Creador'

    def getCosto(self, obj):
        return "${}".format(obj.costo)

    getCosto.short_description = 'Costo'

    def getPesaje(self, obj):
        return "{} kg".format(obj.pesaje)

    getPesaje.short_description = 'Pesaje'

@admin.register(Camion)
class CamionAdmin(admin.ModelAdmin):
    list_display = [ 'patente', 'transportista', 'tara']
    list_display_links = [ 'patente', 'transportista']
    search_fields = ['patente', 'transportista__nombre']
    ordering = ['patente']
    list_per_page = 20
