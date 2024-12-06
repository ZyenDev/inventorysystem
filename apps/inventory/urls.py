from django.urls import path
from . import views

urlpatterns = [
    #productos urls
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/crear/', views.crear_producto, name='crear_producto'),
    path('productos/<int:pk>/actualizar/', views.actualizar_producto, name='actualizar_producto'),
    path('productos/<int:pk>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
    
    #proveedores urls
    path('proveedores/', views.lista_proveedores, name='lista_proveedores'),
    path('proveedores/crear/', views.crear_proveedor, name='crear_proveedor'),
    path('proveedores/<int:pk>/actualizar/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('proveedores/<int:pk>/eliminar/', views.eliminar_proveedor, name='eliminar_proveedor'),
]