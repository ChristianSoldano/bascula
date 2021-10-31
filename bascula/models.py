from django.db import models
from django.contrib.auth.models import User

class Usuario(User):
    created_at = models.DateField(auto_now=True, blank=False, null=False)
    updated_at = models.DateField(auto_now=True, blank=False, null=False)

    class Meta:
        verbose_name_plural = "Usuarios"
        verbose_name = "Usuario"

class Generador(models.Model):    
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250, blank=False, null=False)
    cuit = models.CharField(max_length=100, blank=False, null=False)
    nombre_fantasia = models.CharField(max_length=250, blank=False, null=False)
    f_creacion = models.DateTimeField(auto_now=True, blank=False, null=False)
    activo =  models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Generadores"
        verbose_name = "Generador"
        db_table = "generadores"

class Transportista(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.IntegerField(null=False, blank=False)
    empresa = models.CharField(max_length=250, blank=False, null=False)
    nombre_fantasia = models.CharField(max_length=250, blank=False, null=False)
    cuit = models.CharField(max_length=100, blank=False, null=False)
    activo =  models.IntegerField(null=False, blank=False)
    f_creacion = models.DateTimeField(auto_now=True, blank=False, null=False)

    def __str__(self):
        return self.codigo

    class Meta:
        verbose_name_plural = "Transportistas"
        verbose_name = "Transportista"
        db_table = "transportistas"

class Camion(models.Model):
    id = models.AutoField(primary_key=True)
    patente = models.CharField(max_length=100, blank=False, null=False)
    id_transportista = models.ForeignKey(Transportista, on_delete=models.PROTECT, blank=False, null=False, db_column='id_transportista')
    tara = models.FloatField(null=False, blank=False)
    f_creacion = models.DateTimeField(auto_now=True, blank=False, null=False)
    activo =  models.IntegerField(null=False, blank=False, default=1)

    def __str__(self):
        return self.patente

    class Meta:
        verbose_name_plural = "Camiones"
        verbose_name = "Camion"
        db_table = "camiones"

class Destino(models.Model):
    id = models.AutoField(primary_key=True)
    destino = models.CharField(max_length=250, blank=False, null=False)
    activo =  models.IntegerField(null=False, blank=False, default=1)
    f_creacion = models.DateTimeField(auto_now=True, blank=False, null=False)
    
    def __str__(self):
        return self.destino

    class Meta:
        verbose_name_plural = "Destinos"
        verbose_name = "Destino"
        db_table = "destinos"

class Residuo(models.Model):
    id = models.AutoField(primary_key=True)
    residuo = models.CharField(max_length=250, blank=False, null=False, db_column='residuo')
    activo =  models.IntegerField(null=False, blank=False, default=1)
    f_creacion = models.DateTimeField(auto_now=True, blank=False, null=False)

    def __str__(self):
        return self.residuo

    class Meta:
        verbose_name_plural = "Residuos"
        verbose_name = "Residuo"
        db_table = "residuos"

class Pesaje(models.Model):
    id = models.AutoField(primary_key=True)
    id_generador = models.ForeignKey(Generador, on_delete=models.PROTECT, blank=False, null=False )
    id_residuo = models.ForeignKey(Residuo, on_delete=models.PROTECT, blank=False, null=False )
    id_transportista = models.ForeignKey(Transportista, on_delete=models.PROTECT, blank=False, null=False )
    id_camion = models.ForeignKey(Camion, on_delete=models.PROTECT, blank=False, null=False )
    id_destino = models.ForeignKey(Destino, on_delete=models.PROTECT, blank=False, null=False )
    id_usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, blank=False, null=False )
    pesaje = models.FloatField(null=False, blank=False)
    f_creacion = models.DateTimeField(auto_now=True, blank=False, null=False)
    activo =  models.IntegerField(null=False, blank=False, default=1)    

    def __str__(self):
        return self.patente

    class Meta:
        verbose_name_plural = "Pesajes"
        verbose_name = "Pesaje"
        db_table = "pesajes"

class GeneradoresResiduos(models.Model):
    id = models.AutoField(primary_key=True)
    id_generador = models.ForeignKey(Generador, on_delete=models.PROTECT, blank=False, null=False, db_column='id_generador', name='id_generador')
    id_residuo = models.ForeignKey(Residuo, on_delete=models.PROTECT, blank=False, null=False, db_column='id_residuo', name='id_residuo')
    f_creacion = models.DateTimeField(auto_now=True, blank=False, null=False)
    activo =  models.IntegerField(null=False, blank=False, default=1)

    class Meta:
        verbose_name_plural = "GeneradoresResiduos"
        verbose_name = "GeneradoresResiduos"
        db_table = "generadores_residuos"
        