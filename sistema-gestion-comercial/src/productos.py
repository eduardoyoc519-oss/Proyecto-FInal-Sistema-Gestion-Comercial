
# MODULO DE GESTION DE PRODUCTOS (productos.py)


from archivos import cargar_datos, guardar_datos

nombre_archivo = "productos.json"

def registrar_producto():
    """registra un nuevo producto validando codigos unicos y valores positivos"""
    print("\n-REGISTRAR NUEVO PRODUCTO--")
    productos = cargar_datos(nombre_archivo)
    
    codigo = input("ingrese el codigo unico del producto: ").strip().lower()
    if not codigo:
        print("error: el codigo no puede estar vacio")
        return
    
    for p in productos:
        if p["codigo"] == codigo:
            print(f"error: ya existe un producto con el codigo '{codigo}'")
            return

    nombre = input("ingrese el nombre del producto: ").strip()
    categoria = input("ingrese la categoria: ").strip()
    
    if not nombre or not categoria:
        print("error: el nombre y la categoria son obligatorios")
        return

    try:
        precio_venta = float(input("ingrese el precio de venta (Q): "))
        if precio_venta <= 0:
            print("error: el precio de venta debe ser mayor a 0")
            return
    except ValueError:
        print("error: debe ingresar un valor numerico valido para el precio")
        return

    try:
        cantidad_disponible = int(input("ingrese la cantidad inicial disponible: "))
        if cantidad_disponible < 0:
            print("error: la cantidad no puede ser negativa")
            return
    except ValueError:
        print("error: debe ingresar un numero entero valido")
        return

    try:
        stock_minimo = int(input("ingrese el stock minimo permitido: "))
        if stock_minimo < 0:
            print("error: el stock minimo no puede ser negativo")
            return
    except ValueError:
        print("error: Debe ingresar un numero entero valido")
        return

    nuevo_producto = {
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "precio_venta": precio_venta,
        "cantidad_disponible": cantidad_disponible,
        "stock_minimo": stock_minimo,
        "activo": True 
    }

    productos.append(nuevo_producto)
    
    if guardar_datos(nombre_archivo, productos):
        print(f"¡listo! Producto '{nombre}' registrado correctamente")
    else:
        print("error al guardar el producto")



def consultar_producto_por_codigo():
    """busca un producto por su codigo"""
    print("\n--CONSULTAR PRODUCTO--")
    codigo = input("ingrese el codigo del producto a buscar: ").strip().lower()
    productos = cargar_datos(nombre_archivo)
    
    for p in productos:
        if p["codigo"] == codigo:
            estado = "activo" if p["activo"] else "desactivado"
            print("\n--DETALLES DEL PRODUCTO--")
            print(f"codigo: {p['codigo']}")
            print(f"nombre: {p['nombre']}")
            print(f"categoria: {p['categoria']}")
            print(f"precio de Venta: Q{p['precio_venta']:.2f}")
            print(f"cantidad Disponible: {p['cantidad_disponible']}")
            print(f"stock Minimo: {p['stock_minimo']}")
            print(f"estado: {estado}")
            return
            
    print(f"no se encontro ningun producto con el codigo '{codigo}'")








def listar_productos():
    """muestra el listado general de productos"""
    print("\n--LISTADO GENERAL DE PRODUCTOS--")
    productos = cargar_datos(nombre_archivo)
    
    if not productos:
        print("no hay productos registrados")
        return
        
    print(f"{'CODIGO':<10} | {'NOMBRE':<20} | {'CATEGORIA':<15} | {'PRECIO':<10} | {'STOCK':<8} | {'ESTADO'}")
    print("-" * 80)
    for p in productos:
        estado = "activo" if p["activo"] else "inactivo"
        print(f"{p['codigo']:<10} | {p['nombre']:<20} | {p['categoria']:<15} | Q{p['precio_venta']:<9.2f} | {p['cantidad_disponible']:<8} | {estado}")




def modificar_producto():
    """modifica los datos de un producto existente"""
    print("\n--MODIFICAR PRODUCTO--")
    codigo = input("ingrese el codigo del producto a modificar: ").strip().lower()
    productos = cargar_datos(nombre_archivo)
    
    for p in productos:
        if p["codigo"] == codigo:
            print(f"producto encontrado: {p['nombre']} deje en blanco si no desea cambiar un campo")
            
            nuevo_nombre = input(f"nuevo nombre [{p['nombre']}]: ").strip()
            if nuevo_nombre:
                p["nombre"] = nuevo_nombre
                
            nueva_cat = input(f"nueva categoria [{p['categoria']}]: ").strip()
            if nueva_cat:
                p["categoria"] = nueva_cat
                
            nuevo_precio = input(f"nuevo precio [{p['precio_venta']}]: ").strip()
            if nuevo_precio:
                try:
                    val = float(nuevo_precio)
                    if val > 0: p["precio_venta"] = val
                except ValueError:
                    pass
                    
            nuevo_stock = input(f"nuevo stock minimo [{p['stock_minimo']}]: ").strip()
            if nuevo_stock:
                try:
                    val = int(nuevo_stock)
                    if val >= 0: p["stock_minimo"] = val
                except ValueError:
                    pass
            
            if guardar_datos(nombre_archivo, productos):
                print("producto modificado con exito")
            return
            
    print(f"no se encontro el producto con codigo '{codigo}'")



def desactivar_producto():
    """desactiva un producto para que no este disponible"""
    print("\n--DESACTIVAR PRODUCTO--")
    codigo = input("Ingrese el codigo del producto a desactivar: ").strip().lower()
    productos = cargar_datos(nombre_archivo)
    
    for p in productos:
        if p["codigo"] == codigo:
            p["activo"] = False
            if guardar_datos(nombre_archivo, productos):
                print(f"El producto '{p['nombre']}' fue desactivado")
            return
            
    print(f"No se encontro el producto con codigo '{codigo}'")





