from django.urls import path 
from bascula.views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('historial/', historial, name='historial'),
    path('ajax/GetResiduosbyIdGenerador', GetResiduosbyIdGenerador, name="ResiduosPorGenerador"),
    path('ajax/GetCamionbyIdTransportista', GetCamionbyIdTransportista, name="GetCamionbyIdTransportista"),
    path('ajax/getTara', getTara, name="FijarTara"),
    path('ajax/GuardarPesaje', GuardarPesaje, name="GuardarPesaje"),
    path('ajax/tablahistorial', tablahistorial, name="tablahistorial"),
    path('testing/', testing, name="GuardarPesaje")
    ]