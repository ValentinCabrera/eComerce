from rest_framework import serializers
from .models import Pedido, ItemPedido
from productos.serializer import ProductoSerializer


class ItemPedidoSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer()

    class Meta:
        model = ItemPedido
        fields = '__all__'


class PedidoSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()

    class Meta:
        model = Pedido
        fields = '__all__'

    def get_items(self, obj):
        items = obj.get_items()
        serializer = ItemPedidoSerializer(items, many=True)
        return serializer.data

    def get_total(self, obj):
        return obj.get_total()
