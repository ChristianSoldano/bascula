from django.urls import path 
from bascula.views import *

urlpatterns = [
    path('', home, name='index'),
    ]