from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Categoria, Producto
from .serializer import CategoriaSerializer, ProductoSerializer


class ListarCategorias(APIView):
    """
    Listar categorias
    """

    def get(self, request):
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)

        return Response(serializer.data)


class ListarProductos(APIView):
    """
    Listar productos de una categoria en especifica
    """

    def post(self, request):
        categoria = get_object_or_404(
            Categoria, pk=int(request.data.get("categoria")))
        productos = Producto.objects.filter(categoria=categoria)
        serializer = ProductoSerializer(productos, many=True)

        return Response(serializer.data)
