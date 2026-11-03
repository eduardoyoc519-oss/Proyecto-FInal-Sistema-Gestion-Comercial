
# MODULO DE CONTROL DE INVENTARIO (inventario.py)


from datetime import datetime
from archivos import cargar_datos, guardar_datos

archivo_productos = "productos.json"
archivo_inventario = "inventario.json"



def consultar_existencias():
    """consulta las existencias actuales de todos los productos"""
    print("\n--CONSULTAR EXISTENCIAS DE INVENTARIO--")
    productos = cargar_datos(archivo_productos)
    
    if not productos:
        print("no hay productos registrados")
        return
        
    print(f"{'codigo':<10} | {'nombre':<20} | {'disponible':<12} | {'stock min':<10} | {'estado stock'}")
    print("-" * 65)
    for p in productos:
        stock_estado = "alerta stock" if p["cantidad_disponible"] <= p["stock_minimo"] else "normal"
        print(f"{p['codigo']:<10} | {p['nombre']:<20} | {p['cantidad_disponible']:<12} | {p['stock_minimo']:<10} | {stock_estado}")



def registrar_entrada_inventario():
    """registra una entrada de inventario aumentando la cantidad disponible de un producto"""
    print("\n--REGISTRAR ENTRADA DE INVENTARIO--")
    productos = cargar_datos(archivo_productos)
    
    if not productos:
        print("no hay productos registrados")
        return
        
    codigo = input("ingrese el codigo del producto para entrada:").strip().lower()
    
    producto_encontrado = None
    for p in productos:
        if p["codigo"] == codigo:
            producto_encontrado = p
            break
            
    if not producto_encontrado:
        print("error: el producto no existe")
        return
        
    try:
        cantidad = int(input(f"ingrese la cantidad a ingresar para '{producto_encontrado['nombre']}': "))
        if cantidad <= 0:
            print("error: la cantidad debe ser mayor a cero")
            return
    except ValueError:
        print("error: debe ingresar un numero entero valido")
        return
        
    descripcion = input("ingrese descripcion o motivo de la entrada: ").strip()
    if not descripcion:
        descripcion = "entrada de inventario general"

    producto_encontrado["cantidad_disponible"] += cantidad
    
    historial = cargar_datos(archivo_inventario)
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    historial.append({
        "fecha": fecha_actual,
        "codigo": codigo,
        "tipo": "entrada",
        "cantidad": cantidad,
        "descripcion": descripcion
    })
    
    guardar_datos(archivo_productos, productos)
    guardar_datos(archivo_inventario, historial)
    print(f"¡entrada registrada con exito! nuevo stock de '{producto_encontrado['nombre']}': {producto_encontrado['cantidad_disponible']}")



def consultar_historial_movimientos():
    """consulta el historial completo de movimientos de inventario"""
    print("\n--HISTORIAL DE MOVIMIENTOS DE INVENTARIO--")
    historial = cargar_datos(archivo_inventario)
    
    if not historial:
        print("no hay movimientos registrados en el inventario")
        return
        
    print(f"{'fecha':<20} | {'codigo':<10} | {'tipo':<10} | {'cantidad':<10} | {'descripcion'}")
    print("-" * 75)
    for m in historial:
        print(f"{m['fecha']:<20} | {m['codigo']:<10} | {m['tipo']:<10} | {m['cantidad']:<10} | {m['descripcion']}")




