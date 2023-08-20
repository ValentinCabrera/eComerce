from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Pedido, ItemPedido
from .serializer import PedidoSerializer
from productos.models import Producto


class CrearPedido(APIView):
    """
    Crear un nuevo pedido

    return: pedido
    """

    def get(self, request):
        pedido = Pedido()
        pedido.save()

        serializer = PedidoSerializer(pedido)

        return Response(serializer.data)


class ConfirmarPedido(APIView):
    """
    Confirmar un pedido

    args: pedido
    returns: pedido
    """


class AgregarProducto(APIView):
    """
    Agregar un producto al pedido

    args: pedido, producto, cantidad
    return: pedido
    """

    def post(self, request):
        pedido = get_object_or_404(Pedido, pk=int(request.data.get("pedido")))
        producto = get_object_or_404(
            Producto, pk=int(request.data.get("producto")))
        cantidad = int(request.data.get("cantidad"))
        ingredientes = request.data.get("ingredientes")
        print(ingredientes)

        try:
            item = ItemPedido.objects.get(pedido=pedido, producto=producto)
            item.cantidad += cantidad
            item.save()

            if cantidad == 0 or item.cantidad == 0:
                item.delete()

        except ItemPedido.DoesNotExist:
            item = ItemPedido(
                pedido=pedido, producto=producto, cantidad=cantidad)
            item.save()

        serializer = PedidoSerializer(pedido)
        return Response(serializer.data)
