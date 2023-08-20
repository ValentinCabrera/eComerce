from rest_framework import serializers
from .models import Categoria, Producto, Ingrediente


class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    ingredientes = serializers.SerializerMethodField()

    class Meta:
        model = Producto
        fields = '__all__'

    def get_ingredientes(self, obj):
        ingredientes = obj.get_ingredientes()
        serializer = IngredienteSerializer(ingredientes, many=True)

        return serializer.data
