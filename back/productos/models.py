from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=40, unique=True)
    imagen = models.ImageField(upload_to="productos/static/categorias")
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    imagen = models.ImageField(upload_to="productos/static/productos")
    descripcion = models.TextField()
    stock = models.PositiveSmallIntegerField()
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT)
    precio = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.nombre

    def get_ingredientes(self):
        return map(lambda detalle: detalle.ingrediente, self.detalles.all())


class Ingrediente(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.PositiveSmallIntegerField()
    activo = models.BooleanField()


class DetalleIngrediente(models.Model):
    producto = models.ForeignKey(
        Producto, on_delete=models.RESTRICT, related_name="detalles")
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.RESTRICT)
