
# MODULO DE REGISTRO DE VENTAS (ventas.py)

from datetime import datetime
from archivos import cargar_datos, guardar_datos

archivo_ventas = "ventas.json"
archivo_productos = "productos.json"
archivo_inventario = "inventario.json"


def registrar_venta():
    """registra una venta de productos, calcula subtotales, iva y actualiza inventario"""
    print("\n--REGISTRAR NUEVA VENTA--")
    productos = cargar_datos(archivo_productos)
    
    if not productos:
        print("no hay productos registrados en el sistema")
        return

    carrito = []
    
    while True:
        codigo = input("ingrese el codigo del producto a vender (o escriba 'fin'):").strip().lower()
        if codigo == 'fin':
            break
            
        producto_encontrado = None
        for p in productos:
            if p["codigo"] == codigo:
                producto_encontrado = p
                break
                
        if not producto_encontrado:
            print("error: el producto no existe")
            continue
            
        if not producto_encontrado.get("activo", True):
            print("error: el producto esta desactivado y no se puede vender")
            continue
            
        try:
            cantidad = int(input(f"ingrese la cantidad a vender de '{producto_encontrado['nombre']}':"))
            if cantidad <= 0:
                print("error: la cantidad debe ser mayor a cero")
                continue
        except ValueError:
            print("error: debe ingresar un numero entero valido")
            continue
            
        if cantidad > producto_encontrado["cantidad_disponible"]:
            print(f"error: stock insuficiente. disponible actual: {producto_encontrado['cantidad_disponible']}")
            continue
            
        subtotal = cantidad * producto_encontrado["precio_venta"]
        
        carrito.append({
            "codigo": producto_encontrado["codigo"],
            "nombre": producto_encontrado["nombre"],
            "precio_unitario": producto_encontrado["precio_venta"],
            "cantidad": cantidad,
            "subtotal": subtotal
        })
        
        producto_encontrado["cantidad_disponible"] -= cantidad
        print(f"agregado: {cantidad}x {producto_encontrado['nombre']} - subtotal: Q{subtotal:.2f}")

    if not carrito:
        print("venta cancelada. no se agregaron productos")
        return

    subtotal_general = sum(item["subtotal"] for item in carrito)
    iva = subtotal_general * 0.12
    total = subtotal_general + iva

    ventas = cargar_datos(archivo_ventas)
    numero_venta = f"v-{len(ventas) + 1:04d}"
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    historial_inventario = cargar_datos(archivo_inventario)
    for item in carrito:
        historial_inventario.append({
            "fecha": fecha_actual,
            "codigo": item["codigo"],
            "tipo": "salida",
            "cantidad": item["cantidad"],
            "descripcion": f"venta {numero_venta}"
        })





    guardar_datos(archivo_productos, productos)
    guardar_datos(archivo_inventario, historial_inventario)

    nueva_venta = {
        "numero_venta": numero_venta,
        "fecha": fecha_actual,
        "items": carrito,
        "subtotal": subtotal_general,
        "iva": iva,
        "total": total
    }
    ventas.append(nueva_venta)
    guardar_datos(archivo_ventas, ventas)


    print("\n" + "="*45)
    print(f"       comprobante de venta: {numero_venta}")
    print("="*45)
    print(f"fecha: {fecha_actual}")
    print("-"*45)
    for item in carrito:
        print(f"- {item['cantidad']}x {item['nombre']} (Q{item['precio_unitario']:.2f}) = Q{item['subtotal']:.2f}")
    print("-"*45)
    print(f"subtotal general: Q{subtotal_general:.2f}")
    print(f"iva (12%):        Q{iva:.2f}")
    print(f"total a pagar:    Q{total:.2f}")
    print("="*45)
    print("¡venta registrada y stock actualizado con exito!")



def consultar_historial_ventas():
    """muestra el listado historico de todas las ventas realizadas"""
    print("\n--HISTORIAL DE VENTAS--")
    ventas = cargar_datos(archivo_ventas)
    
    if not ventas:
        print("no hay ventas registradas en el sistema")
        return
        
    for v in ventas:
        print(f"\nventa no: {v['numero_venta']} | fecha: {v['fecha']}")
        print(f"{'producto':<20} | {'cantidad':<10} | {'precio':<10} | {'subtotal'}")
        print("-" * 55)
        for i in v['items']:
            print(f"{i['nombre']:<20} | {i['cantidad']:<10} | Q{i['precio_unitario']:<9.2f} | Q{i['subtotal']:.2f}")
        print(f"subtotal: Q{v['subtotal']:.2f} | iva: Q{v['iva']:.2f} | total: Q{v['total']:.2f}")
        print("=" * 55)



