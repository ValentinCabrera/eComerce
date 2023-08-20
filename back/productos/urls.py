from django.urls import path
from .views import *

app_name = 'productos'

urlpatterns = [
    path('categorias/', ListarCategorias.as_view()),
    path('productos/', ListarProductos.as_view()),
]
