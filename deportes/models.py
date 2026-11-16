from django.db import models


class Producto(models.Model):
    OPCIONES_CATEGORIA = [
        ('Calzado', 'Calzado'),
        ('Ropa', 'Ropa'),
        ('Accesorios', 'Accesorios'),
        ('Equipamiento', 'Equipamiento'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    stock = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_ingreso = models.DateField()
    categoria = models.CharField(max_length=50, choices=OPCIONES_CATEGORIA)

    def __str__(self):
        return self.nombre