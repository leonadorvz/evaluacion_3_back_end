from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_productos, name='listar_productos'),
    path('buscar/', views.buscar_producto, name='buscar_producto'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('modificar/<int:id_producto>/', views.modificar_producto, name='modificar_producto'),
    path('eliminar/<int:id_producto>/', views.eliminar_producto, name='eliminar_producto'),
    path('login/', views.iniciar_sesion, name='iniciar_sesion'),
    path('logout/', views.cerrar_sesion, name='cerrar_sesion'),
]