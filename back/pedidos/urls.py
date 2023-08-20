from django.urls import path
from .views import *

app_name = 'pedidos'

urlpatterns = [
    path('crear/', CrearPedido.as_view()),
    path('agregar/', AgregarProducto.as_view()),
]
