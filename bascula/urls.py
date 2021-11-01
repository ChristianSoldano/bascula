from django.urls import path 
from bascula.views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('login/', login, name='login'),
    path('ajax/GetResiduosbyIdGenerador', GetResiduosbyIdGenerador, name="ResiduosPorGenerador"),
    path('ajax/GetVehiculobyIdTransportista', GetVehiculobyIdTransportista, name="GetVehiculobyIdTransportista"),
    path('ajax/FijarTara', FijarTara, name="FijarTara"),
    path('ajax/GuardarPesaje', GuardarPesaje, name="GuardarPesaje"),
    ]