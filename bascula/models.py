from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, RegexValidator


class Usuario(User):
    class Meta:
        proxy = True
        verbose_name_plural = "Usuarios"
        verbose_name = "Usuario"

    def toJson(self):
        return {'id': self.id, 'username': self.username, 'nombre': self.first_name, 'apellido': self.last_name,
                'admin': self.is_superuser, 'fcreacion': self.date_joined.strftime('%Y-%m-%d %H:%M'), 'activo': self.is_active}

class Residuo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(
        max_length=255, blank=False, null=False, unique=True)
    costo_tonelada = models.FloatField(blank=False, null=False, validators=[
                                       MinValueValidator(1, message='El costo de la tonelada no puede ser menor a $1')])
    fcreacion = models.DateTimeField(auto_now=True, blank=False, null=False)
    activo = models.BooleanField(blank=False, null=False, default=True)

    def __str__(self):
        return self.nombre

    def toJson(self):
        return {'id': self.id, 'nombre': self.nombre, 'costo_tonelada': self.costo_tonelada,
                'fcreacion': self.fcreacion.strftime('%Y-%m-%d %H:%M'), 'activo': self.activo}

    class Meta:
        verbose_name_plural = "Residuos"
        verbose_name = "Residuo"
        db_table = "residuos"


class Generador(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(
        max_length=255, blank=False, null=False, unique=True)
    nombre_fantasia = models.CharField(
        max_length=255, blank=False, null=False, unique=True)
    cuit = models.CharField(max_length=13, blank=False, null=False, unique=True, validators=[RegexValidator(
        regex='^(20|23|24|25|26|27|30|33|34)(-)(\D)?[0-9]{8}(-)(\D)?[0-9]$', message="Formato de cuit inválido")])
    residuos = models.ManyToManyField(Residuo)
    fcreacion = models.DateTimeField(auto_now=True, blank=False, null=False)
    activo = models.BooleanField(blank=False, null=False, default=True)

    def __str__(self):
        return self.nombre

    def toJson(self):
        return {'id': self.id, 'nombre': self.nombre, 'cuit': self.cuit, 'nombre_fantasia': self.nombre_fantasia,
                'fcreacion': self.fcreacion.strftime('%Y-%m-%d %H:%M'), 'activo': self.activo}

    class Meta:
        verbose_name_plural = "Generadores"
        verbose_name = "Generador"
        db_table = "generadores"


class Transportista(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.PositiveIntegerField(null=False, blank=False, unique=True)
    nombre = models.CharField(
        max_length=255, blank=False, null=False, unique=True)
    nombre_fantasia = models.CharField(
        max_length=255, blank=False, null=False, unique=True)
    cuit = models.CharField(max_length=13, blank=False, null=False, unique=True, validators=[RegexValidator(
        regex='^(20|23|24|25|26|27|30|33|34)(-)(\D)?[0-9]{8}(-)(\D)?[0-9]$', message="Formato de cuit inválido")])
    fcreacion = models.DateTimeField(auto_now=True, blank=False, null=False)
    activo = models.BooleanField(blank=False, null=False, default=True)

    def __str__(self):
        return self.nombre

    def toJson(self):
        return {'id': self.id, 'codigo': self.codigo, 'nombre': self.nombre, 'nombre_fantasia': self.nombre_fantasia,
                'cuit': self.cuit, 'fcreacion': self.fcreacion.strftime('%Y-%m-%d %H:%M'), 'activo': self.activo}

    class Meta:
        verbose_name_plural = "Transportistas"
        verbose_name = "Transportista"
        db_table = "transportistas"


class Camion(models.Model):
    id = models.AutoField(primary_key=True)
    patente = models.CharField(
        max_length=7, blank=False, null=False, unique=True)
    transportista = models.ForeignKey(Transportista, on_delete=models.PROTECT,
                                      blank=False, null=False, db_column='codigo_transportista', to_field='codigo')
    tara = models.FloatField(null=False, blank=False)
    fcreacion = models.DateTimeField(auto_now=True, blank=False, null=False)
    activo = models.BooleanField(blank=False, null=False, default=True)

    def __str__(self):
        return self.patente

    def toJson(self):
        return {'id': self.id, 'patente': self.patente, 'codigo_transportista': self.transportista.codigo,
                'tara': self.tara, 'fcreacion': self.fcreacion.strftime('%Y-%m-%d %H:%M'), 'activo': self.activo}

    class Meta:
        verbose_name_plural = "Camiones"
        verbose_name = "Camion"
        db_table = "camiones"


class Destino(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(
        max_length=255, blank=False, null=False, unique=True)
    fcreacion = models.DateTimeField(auto_now=True, blank=False, null=False)
    activo = models.BooleanField(blank=False, null=False, default=True)

    def __str__(self):
        return self.nombre

    def toJson(self):
        return {'id': self.id, 'nombre': self.nombre,
                'fcreacion': self.fcreacion.strftime('%Y-%m-%d %H:%M'), 'activo': self.activo}

    class Meta:
        verbose_name_plural = "Destinos"
        verbose_name = "Destino"
        db_table = "destinos"


class Pesaje(models.Model):
    id = models.AutoField(primary_key=True)
    generador = models.CharField(max_length=255, blank=False, null=False)
    residuo = models.CharField(max_length=255, blank=False, null=False)
    transportista = models.CharField(max_length=255, blank=False, null=False)
    camion = models.CharField(max_length=255, blank=False, null=False)
    destino = models.CharField(max_length=255, blank=False, null=False)    
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, blank=False, null=False, db_column='id_usuario')
    pesaje = models.FloatField(null=False, blank=False)
    costo = models.FloatField(null=False, blank=False)
    fcreacion = models.DateTimeField(auto_now=True, blank=False, null=False)
    activo = models.BooleanField(blank=False, null=False, default=True)

    def toJson(self):
        return {'id': self.id, 'generador': self.generador, 'residuo': self.residuo,
                'transportista': self.transportista, 'camion': self.camion, 'destino': self.destino,
                'id_usuario': 1, 'pesaje': self.pesaje, 'costo': self.costo, 'fcreacion': self.fcreacion.strftime('%Y-%m-%d %H:%M'),
                'activo': self.activo}

    class Meta:
        verbose_name_plural = "Pesajes"
        verbose_name = "Pesaje"
        db_table = "pesajes"


# class GeneradoresResiduos(models.Model):
#     id = models.AutoField(primary_key=True)
#     generador = models.ForeignKey(
#         Generador, on_delete=models.PROTECT, blank=False, null=False, db_column='id_generador')
#     residuo = models.ForeignKey(
#         Residuo, on_delete=models.PROTECT, blank=False, null=False, db_column='id_residuo')
#     fcreacion = models.DateTimeField(auto_now=True, blank=False, null=False)
#     activo = models.BooleanField(blank=False, null=False, default=True)

#     def toJson(self):
#         return {'id': self.id, 'id_generador': self.generador.id, 'id_residuo': self.residuo.id,
#                 'fcreacion': self.fcreacion.strftime('%Y-%m-%d %H:%M'), 'activo': self.activo}

#     class Meta:
#         verbose_name_plural = "GeneradoresResiduos"
#         verbose_name = "GeneradoresResiduos"
#         db_table = "generadores_residuos"
