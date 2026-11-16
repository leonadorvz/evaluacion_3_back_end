from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Producto
from .forms import FormularioProducto


def iniciar_sesion(request):
    if request.user.is_authenticated:
        return redirect('listar_productos')

    if request.method == 'POST':
        nombre_usuario = request.POST.get('username')
        clave_usuario = request.POST.get('password')
        usuario = authenticate(request, username=nombre_usuario, password=clave_usuario)

        if usuario is not None:
            login(request, usuario)
            return redirect('listar_productos')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')

    return render(request, 'deportes/iniciar_sesion.html')


def cerrar_sesion(request):
    logout(request)
    return redirect('iniciar_sesion')


@login_required(login_url='iniciar_sesion')
def listar_productos(request):
    productos = Producto.objects.all().order_by('id')
    return render(request, 'deportes/listar.html', {'productos': productos})


@login_required(login_url='iniciar_sesion')
def buscar_producto(request):
    termino = request.GET.get('nombre', '').strip()
    productos = []
    busqueda_realizada = False

    if termino != '':
        productos = Producto.objects.filter(nombre__icontains=termino)
        busqueda_realizada = True

    datos = {
        'productos': productos,
        'termino': termino,
        'busqueda_realizada': busqueda_realizada
    }
    return render(request, 'deportes/buscar.html', datos)


@login_required(login_url='iniciar_sesion')
def agregar_producto(request):
    if not request.user.is_superuser:
        messages.error(request, 'Acceso denegado: Solo el administrador puede agregar productos.')
        return redirect('listar_productos')

    if request.method == 'POST':
        formulario = FormularioProducto(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            nuevo_producto = Producto(
                nombre=datos['nombre'],
                descripcion=datos['descripcion'],
                stock=datos['stock'],
                precio_unitario=datos['precio_unitario'],
                fecha_ingreso=datos['fecha_ingreso'],
                categoria=datos['categoria']
            )
            nuevo_producto.save()
            messages.success(request, 'Producto agregado exitosamente.')
            return redirect('listar_productos')
    else:
        formulario = FormularioProducto()

    return render(request, 'deportes/agregar.html', {'formulario': formulario})


@login_required(login_url='iniciar_sesion')
def modificar_producto(request, id_producto):
    if not request.user.is_superuser:
        messages.error(request, 'Acceso denegado: Solo el administrador puede modificar productos.')
        return redirect('listar_productos')

    producto = Producto.objects.get(id=id_producto)

    if request.method == 'POST':
        formulario = FormularioProducto(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            producto.nombre = datos['nombre']
            producto.descripcion = datos['descripcion']
            producto.stock = datos['stock']
            producto.precio_unitario = datos['precio_unitario']
            producto.fecha_ingreso = datos['fecha_ingreso']
            producto.categoria = datos['categoria']
            producto.save()
            messages.success(request, 'Producto modificado exitosamente.')
            return redirect('listar_productos')
    else:
        datos_iniciales = {
            'nombre': producto.nombre,
            'descripcion': producto.descripcion,
            'stock': producto.stock,
            'precio_unitario': producto.precio_unitario,
            'fecha_ingreso': producto.fecha_ingreso,
            'categoria': producto.categoria
        }
        formulario = FormularioProducto(initial=datos_iniciales)

    return render(request, 'deportes/modificar.html', {'formulario': formulario, 'producto': producto})


@login_required(login_url='iniciar_sesion')
def eliminar_producto(request, id_producto):
    if not request.user.is_superuser:
        messages.error(request, 'Acceso denegado: Solo el administrador puede eliminar productos.')
        return redirect('listar_productos')

    producto = Producto.objects.get(id=id_producto)

    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado exitosamente.')
        return redirect('listar_productos')

    return render(request, 'deportes/eliminar.html', {'producto': producto})
