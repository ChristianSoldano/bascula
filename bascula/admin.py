from django import forms
from django.contrib import admin
from bascula import *
from bascula.models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Group


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmación de contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('username', 'nombre', 'apellido')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Las contraseñas no son iguales")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Usuario
        fields = ('username', 'nombre', 'apellido', 'admin', 'activo')

class UsuarioAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ['id', 'get_username', 'fullname', 'admin']
    search_fields = ['nombre', 'apellido', 'username ']
    list_display_links = ['id','get_username']
    list_filter = ('admin',)

    fieldsets = (
        (None, {'fields': ('username', 'password', 'activo')}),
        ('Información personal', {'fields': ('nombre','apellido')}),
        ('Permisos', {'fields': ('admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password', 'activo', 'nombre','apellido', 'admin'),
        }),
    )

    def fullname(self, obj):
        return "{} {}".format(obj.nombre, obj.apellido)

    def get_username(self, obj):
        return obj.username

    fullname.short_description = 'Nombre'
    get_username.short_description = 'Usuario'

    search_fields = ('username', 'fullname')
    ordering = ('username',)
    filter_horizontal = ()
    
@admin.register(Generador)
class GeneradorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'nombreFantasia', 'cuit']
    list_display_links = ['id','nombre']
    search_fields = ['nombre', 'nombreFantasia', 'cuit ']
    ordering = ['nombre']

    def nombreFantasia(self, obj):
        return obj.nombre_fantasia

    nombreFantasia.short_description = 'Nombre de Fantasia'

@admin.register(Transportista)
class GeneradorAdmin(admin.ModelAdmin):
    list_display = ['id', 'codigo' ,'nombre', 'nombreFantasia', 'cuit']
    list_display_links = ['id', 'codigo' ,'nombre']
    search_fields = ['nombre', 'nombreFantasia', 'cuit', 'codigo']
    ordering = ['nombre']

    def nombreFantasia(self, obj):
        return obj.nombre_fantasia

    nombreFantasia.short_description = 'Nombre de Fantasia'

@admin.register(Destino)
class GeneradorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    list_display_links = ['id', 'nombre']
    search_fields = ['nombre']
    ordering = ['nombre']

    
@admin.register(Residuo)
class GeneradorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'costoTonelada']
    list_display_links = ['id', 'nombre']
    search_fields = ['nombre']
    ordering = ['nombre']

    def costoTonelada(self, obj):
        return "${}".format(obj.costo_tonelada)

    costoTonelada.short_description = 'Costo Tonelada'


@admin.register(Pesaje)
class GeneradorAdmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(GeneradoresResiduos)
class GeneradorAdmin(admin.ModelAdmin):
    list_display = ['id']

admin.site.register(Usuario, UsuarioAdmin)
admin.site.unregister(Group)