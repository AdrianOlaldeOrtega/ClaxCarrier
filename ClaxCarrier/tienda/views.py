from asyncio.windows_events import NULL
from datetime import date
from django.shortcuts import redirect, render
from tienda.Carrito import Carrito
from .models import Producto, Venta, Cliente, ArticuloVendido
# Create your views here.
#HOME
def index(request):
    return render(request, 'index.html')

def contacto(request):
    return render(request, 'contacto.html')

def producto(request):
    vigilancia = Producto.objects.filter(categoria="Videovigilancia")[:3]
    redes = Producto.objects.filter(categoria="Redes Computacionales")[:3]
    energia = Producto.objects.filter(categoria="Energias Limpias")[:3]
    return render(request, 'producto.html', {"vigilancia":vigilancia, "redes":redes,"energia":energia})

def catalogo(request, categoria):
    if categoria == 1:
        productos = Producto.objects.filter(categoria="Videovigilancia")
    if categoria == 2:
        productos = Producto.objects.filter(categoria="Redes Computacionales")
    if categoria == 3:
        productos = Producto.objects.filter(categoria="Energias Limpias")

    return render(request, 'productosTodo.html', {"vigilancia":productos})

def detalles(request, id):
    producto = Producto.objects.get(id=id)
    return render(request, 'detallesProducto.html',{"producto":producto})

#CARRITO
def carrito(request):
    return render(request, 'carrito.html')

def agregar_producto(request):
    post = Producto()
    if request.method == 'POST':    
        id = request.POST["idProductoO"]    
        cantidad = request.POST["cantidad"]
    carrito = Carrito(request)
    producto = Producto.objects.get(id=id)
    carrito.agregar(producto,cantidad)
    return redirect('verCarrito')

def sumar_producto(request, id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=id)
    carrito.suma(producto)
    return redirect('verCarrito')

def eliminar_producto(request, id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=id)
    carrito.eliminar(producto.id)
    return redirect('producto')

def restar_producto(request, id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=id)
    carrito.restar(producto)
    return redirect('verCarrito')

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('producto')

#COMPRAS
def compra(request):
    return render(request, 'finalizarCompra.html')
    
def graciasCompra(request):
    return render(request, 'graciasCompra.html')

def guardarVenta(request):
    venta = Venta()
    cliente = Cliente()
    articulo = ArticuloVendido()
    carrito = Carrito(request)
    if request.method == 'POST':
        cliente.nombreCliente = request.POST["firstName"]
        cliente.apellidoCliente = request.POST["lastName"]
        cliente.email = request.POST["email"]
        cliente.Domicilio = request.POST["address"]
        cliente.infoAdicional = request.POST["address2"]
        cliente.estado = request.POST["state"]
        cliente.pais = request.POST["country"]
        cliente.codigoPostal = request.POST["zip"]
        cliente.save() 
        clien = Cliente.objects.all().order_by('-id')[:1]
        for c in clien:
            venta.idCliente = c.id
        venta.formaPago = request.POST["paymentMethod"]
        venta.fechaRealizada = date.today().strftime('%Y-%m-%d')
        venta.nombrePropietario = request.POST["cc-name"]
        venta.numeroTarjeta = request.POST["cc-number"]
        venta.vencimiento = request.POST["cc-expiration"]
        venta.cvv = request.POST["cc-cvv"]
        venta.status = "Pendiente"
        venta.total = carrito.total()
        venta.save()
        articulos = carrito.cantidadArticulo()
        for articulo in articulos:
            print(articulo)
            carrito.articulo(articulo)
        
    carrito.limpiar()
    return redirect('graciasCompra')

#ALMACENISTA
def almacenHome(request):
    productos = Producto.objects.all().order_by('stock')
    return render(request, "almacenHome.html", {"productos":productos})

def nuevoProducto(request):
    return render(request, 'InsertarProducto.html')

def guardarProducto(request):
    post = Producto()
    if request.method == 'POST':
        post.nombre = request.POST["NombreProducto"]
        post.descripcion = request.POST["DescripcionProducto"]
        post.categoria = request.POST["CategoriaProducto"]
        post.precio = request.POST["PrecioProducto"]
        post.stock = request.POST["StockProducto"]
        post.urlImagen = request.POST["URLImagenProducto"]
        post.save() 
    return redirect('almacenHome')

def editarProducto(request, id):
    producto = Producto.objects.get(id=id)
    return render(request, "editarProducto.html", {"producto": producto})

def actualizarProducto(request, id):
    post = Producto.objects.get(id=id)
    if request.method == 'POST':
        post.nombre = request.POST["NombreProducto"]
        post.descripcion = request.POST["DescripcionProducto"]
        post.categoria = request.POST["CategoriaProducto"]
        post.precio = request.POST["PrecioProducto"]
        post.urlImagen = request.POST["URLImagenProducto"]
        post.save()
    return redirect('almacenHome')

def editarStock(request, id):
    producto = Producto.objects.get(id=id)
    return render(request, "restockProducto.html", {"producto": producto})

def actualizarStock(request, id):
    post = Producto.objects.get(id=id)
    stock = post.stock
    restock = int(request.POST["StockProducto"])
    stockTotal = stock + restock
    if request.method == 'POST':
        post.stock = stockTotal
        post.save()
    return redirect('almacenHome')

def bajaProducto(request, id):
    producto = Producto.objects.get(id=id)
    return render(request, "eliminarProducto.html", {"producto":producto})

def eliminarProducto(request, id):
    post = Producto.objects.get(id=id)
    post.delete()
    return redirect('almacenHome')

def filtroNombre(request):
    if request.method == 'POST':
        nombre = request.POST["nombre"]
        post = Producto.objects.filter(nombre=nombre).order_by('stock')
    return render(request, "buscarProducto.html", {"productos":post})

def filtroCategoria(request):
    if request.method == 'POST':
        categoria = request.POST["CategoriaProducto"]
        post = Producto.objects.filter(categoria=categoria).order_by('stock')
    return render(request, "buscarProducto.html", {"productos":post})

def filtroStock(request):
    if request.method == 'POST':
        stock = request.POST["stock"]
        post = Producto.objects.filter(stock__lte=stock).order_by('stock')
    return render(request, "buscarProducto.html", {"productos":post})

#ADMINISTRADOR
def adminHome(request):
    ventas = Venta.objects.all().order_by('fechaRealizada')
    return render(request, "adminHome.html", {"ventas":ventas})