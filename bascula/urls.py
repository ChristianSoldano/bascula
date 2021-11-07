from django.urls import path
from bascula.views import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name="login"),
    path('logout/', logout_request, name='logout'),
    path('inicio/', login_required(home), name='home'),
    path('pesajes/', login_required(pesajes), name='pesajes'),
    path('ajax/GetResiduosbyIdGenerador', login_required(GetResiduosbyIdGenerador), name="ResiduosPorGenerador"),
    path('ajax/GetCamionbyIdTransportista', login_required(GetCamionbyIdTransportista), name="GetCamionbyIdTransportista"),
    path('ajax/getTara', login_required(getTara), name="FijarTara"),
    path('ajax/GuardarPesaje', login_required(GuardarPesaje), name="GuardarPesaje"),
    ]