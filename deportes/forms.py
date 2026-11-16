from django import forms
from .models import Producto


class FormularioProducto(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del producto'})
    )
    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción detallada'})
    )
    stock = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '0'})
    )
    precio_unitario = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'})
    )
    fecha_ingreso = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    categoria = forms.ChoiceField(
        choices=Producto.OPCIONES_CATEGORIA,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
