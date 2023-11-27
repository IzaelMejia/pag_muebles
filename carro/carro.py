class Carro:
    # constructor inica tareas Importantes (Peticion acceder al carro ,contruir session, constuir carrito)
    # self, que hace referencia a la instancia de la clase en la que se llama el método.
    # constructor -Se encarga de inicializar la instancia de la clase y almacenar la solicitud (request) actual
    def __init__(self, request):
        self.request = request #almacenar peticion actual 
        self.session = request.session
        carro = self.session.get("carro")  #Contruir carro de la compra, string para identificar carro 
        # Si no tiene carro que lo cree y si tiene carro que muestre el carrito que tiene acumulado
        if not carro:
            carro = self.session["carro"] = {}  #carro vacio
        
        self.carro = carro

    # Metodo Agregar producto al carro
    def agregar(self, producto):             #keys:metodo ver claves
        if str(producto.id) not in self.carro.keys():  # si el producto no esta en el carro (no encuentra esa id)
            self.carro[producto.id] = {  # agregar producto al carro (id del producto a agregar)
                # Este es el diccionario de cada producto
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url,
            }
        else:  #si el producto esta en el carro (incrementar)
            for key, value in self.carro.items():  #recorrer claves valores que tenemos en el carro 
                if key == str(producto.id):   #si la clave(id) corresponde a la del producto a agregar
                    value["cantidad"] = value["cantidad"] + 1   
                    value["precio"] = float(value["precio"]) + producto.precio  #se suma precio                
                    break
        self.guardar_carro()
        
    
    # Carro es diccionario , cada producto con sus caracteristicas 
    # Clave es el id del producto y valor ediccioanrio con caracteristicas del producto
    #  id:{nombre,precio,imagen...}

    # Actualizar cantidad del producto (guardar)
    def guardar_carro(self):
        self.session["carro"] = self.carro #actualizar carrito de acuerdo a la sesión actual
        self.session.modified = True       #Se modifico la sesión? SI
    
    # Eliminar producto del carro
    def eliminar(self, producto):
        producto.id = str(producto.id)  
        if producto.id in self.carro:   #comprobar si el id que queremos eliminar esta en carrito
            del self.carro[producto.id]     #eliminar del carrito el id 
            self.guardar_carro()        #volver a guardar carro
    
    # Eliminar uniadades de un producto
    def restar_producto(self, producto):
        for key, value in self.carro.items():
            if key == str(producto.id):
                value["cantidad"] = value["cantidad"] - 1 #restar cantidad producto -1
                value["precio"] = float(value["precio"]) - producto.precio #restar el precio 
                if value["cantidad"] < 1:  #si la cantidad es menor a 1 eliminalo
                    self.eliminar(producto)
                break
        self.guardar_carro()
    
    
    # Limpiar carrito 
    def limpiar_carro(self):
        self.session["carro"] = {}
        self.session.modified = True

