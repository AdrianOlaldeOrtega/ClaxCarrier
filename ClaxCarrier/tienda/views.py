from asyncio.windows_events import NULL
from django.shortcuts import redirect, render
from .models import Producto
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

#ALMACENISTA
def almacenHome(request):
    productos = Producto.objects.all().order_by('id')
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
        post = Producto.objects.filter(nombre__unaccent__icontains=nombre)
    return render(request, "buscarProducto.html", {"productos":post})

def filtroCategoria(request):
    if request.method == 'POST':
        categoria = request.POST["CategoriaProducto"]
        post = Producto.objects.filter(categoria=categoria)
    return render(request, "buscarProducto.html", {"productos":post})

def filtroStock(request):
    if request.method == 'POST':
        stock = request.POST["stock"]
        post = Producto.objects.filter(stock__lte=stock)
    return render(request, "buscarProducto.html", {"productos":post})
