from django.urls import path 
from bascula.views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('historial/', historial, name='historial'),
    path('ajax/GetResiduosbyIdGenerador', GetResiduosbyIdGenerador, name="ResiduosPorGenerador"),
    path('ajax/GetVehiculobyIdTransportista', GetVehiculobyIdTransportista, name="GetVehiculobyIdTransportista"),
    path('ajax/FijarTara', FijarTara, name="FijarTara"),
    path('ajax/GuardarPesaje', GuardarPesaje, name="GuardarPesaje"),
    path('ajax/tablahistorial', tablahistorial, name="tablahistorial"),
    ]