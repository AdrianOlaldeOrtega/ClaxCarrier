from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from tienda import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('productos/', views.producto, name='producto'),
    path('catalogo/<int:categoria>', views.catalogo, name='verCatalogo'),
    path('detallesProducto/<int:id>', views.detalles, name='verDetalles'),
    
    #CARRITO
    path('carrito/', views.carrito, name='verCarrito'),
    path('agregarProducto/', views.agregar_producto, name="agregarProducto"),
    path('eliminarProductoC/<int:id>', views.eliminar_producto, name="eliminarProductoCarrito"),
    path('sumarProducto/<int:id>', views.sumar_producto, name="sumarProductoCarrito"),
    path('restarProducto/<int:id>', views.restar_producto, name="restarProductoCarrito"),
    path('limpiarLista/', views.limpiar_carrito, name="limpiarCarrito"),

    #FINALIZAR COMPRA
    path('comprar/', views.compra, name="finalizarCompra"),
    path('final/', views.graciasCompra, name="graciasCompra"),
    path('finalizo/', views.guardarVenta, name="guardarVenta"),

    #ALMACENISTA
    path("almacen/", views.almacenHome, name="almacenHome"),
    path('producto/', views.nuevoProducto, name="nuevoProducto"),
    path('newProducto/', views.guardarProducto, name='guardarProducto'),
    path('modificacionProducto/<int:id>', views.editarProducto, name='editarProducto'),
    path('actualizarProducto/<int:id>', views.actualizarProducto, name="actualizarProducto"),
    path('eliminarProducto/<int:id>', views.bajaProducto, name="bajaProducto"),
    path('bajaProducto/<int:id>', views.eliminarProducto, name="eliminarProducto"),
    path('modificacionStock/<int:id>', views.editarStock, name='editarStock'),
    path('actualizarStock/<int:id>', views.actualizarStock, name="actualizarStock"),
    path('filtroNombre/', views.filtroNombre, name="buscarNombreProducto"),
    path('filtroCategoria/', views.filtroCategoria, name="buscarCategoriaProducto"),
    path('filtroStock/', views.filtroStock, name="buscarStockProducto"),

    #ADMINISTRADOR
    path("administrador/", views.adminHome, name="adminHome"),
    
]