from .models import Producto, Venta, Cliente, ArticuloVendido

class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else: 
            self.carrito = carrito

    def suma(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            stock = producto.stock
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += producto.precio
            if self.carrito[id]["cantidad"] > stock:
                self.carrito[id]["cantidad"] -= 1
                self.carrito[id]["acumulado"] -= producto.precio
        self.guardar_carrito()

    def agregar(self, producto,cantidad):
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "acumulado": (int(cantidad) * producto.precio),
                "precio": producto.precio,
                "subtotal":(int(cantidad) * producto.precio),
                "cantidad": int(cantidad),
                "url": producto.urlImagen
            }
        else:
            stock = producto.stock
            self.carrito[id]["cantidad"] += int(cantidad)
            self.carrito[id]["acumulado"] += (int(cantidad) * producto.precio)
            if self.carrito[id]["cantidad"] > stock:
                self.carrito[id]["cantidad"] = stock
                self.carrito[id]["acumulado"] = (producto.precio*stock)
        self.guardar_carrito()
    
    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True
    
    def eliminar(self, producto):
        id = str(producto)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()
    
    def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= producto.precio
            if self.carrito[id]["cantidad"] <= 0: 
                self.carrito[id]["cantidad"] += 1
                self.carrito[id]["acumulado"] += producto.precio
        self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True

    def total(self):
        carrito = self.session["carrito"]
        total = 200
        for key, value in self.session["carrito"].items():
                total += int(value["acumulado"])
        return total

    def articulo(self, id2):
        id = str(id2)
        articulo = ArticuloVendido()
        vent = Venta.objects.all().order_by('-id')[:1]
        if id in self.carrito.keys():
            for v in vent:
                articulo.folioVenta = v.id
            articulo.articulo = self.carrito[id]["nombre"]
            articulo.cantidad = int(self.carrito[id]["cantidad"])
            articulo.subtotal = float(self.carrito[id]["acumulado"])
            post = Producto.objects.get(id=self.carrito[id]["producto_id"])
            stock = post.stock
            restock = int(self.carrito[id]["cantidad"])
            stockTotal = stock - restock
            post.stock = stockTotal
            post.save()
            articulo.save()

    def cantidadArticulo(self):
        articulos = []
        for key, value in self.session["carrito"].items():
                articulos.append(int(value["producto_id"]))
        print(articulos)
        return articulos
        