from django.db import models
from usuarios.models import Cliente, Cadete
from productos.models import Producto, Ingrediente


class Estado(models.Model):
    nombre = models.CharField(max_length=40)


class Pedido(models.Model):
    cliente = models.ForeignKey(
        Cliente, on_delete=models.RESTRICT, blank=True, null=True)
    cadete = models.ForeignKey(
        Cadete, on_delete=models.RESTRICT, blank=True, null=True)

    def __str__(self):
        return str(self.id)

    def get_items(self):
        return self.items.all()

    def get_total(self):
        items = self.get_items()

        total = 0

        for item in items:
            total += item.producto.precio * item.cantidad

        return total


class CambioEstado(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.RESTRICT)
    estado = models.ForeignKey(Estado, on_delete=models.RESTRICT)
    fecha_hora = models.DateTimeField()


class ItemPedido(models.Model):
    pedido = models.ForeignKey(
        Pedido, on_delete=models.RESTRICT, related_name="items")
    producto = models.ForeignKey(Producto, on_delete=models.RESTRICT)
    cantidad = models.PositiveSmallIntegerField()

    def get_item(self):
        return {"producto": self.producto, "cantidad": self.cantidad}

    def get_detalle(self):
        detalles = self.detalles.all()
        return map(lambda detalle: detalle.ingredeinte)


class DetalleItem(models.Model):
    item_pedido = models.ForeignKey(
        ItemPedido, on_delete=models.RESTRICT, related_name="detalles")
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.RESTRICT)
    cantidad = models.PositiveSmallIntegerField()
