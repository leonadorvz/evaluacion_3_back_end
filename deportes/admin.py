from django.contrib import admin
from .models import Producto


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'categoria', 'precio_unitario', 'stock', 'fecha_ingreso')
    search_fields = ('nombre', 'categoria')
    list_filter = ('categoria',)


admin.site.register(Producto, ProductoAdmin)