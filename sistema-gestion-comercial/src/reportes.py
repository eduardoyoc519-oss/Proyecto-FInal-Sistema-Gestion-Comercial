
# MODULO DE REPORTES Y ESTADISTICAS (reportes.py)


from archivos import cargar_datos

archivo_productos = "productos.json"
archivo_ventas = "ventas.json"

def generar_reportes_menu():
    """menu secundario para la generacion de reportes requeridos"""
    while True:
        print("\n========================================")
        print("       MODULO DE REPORTES Y ESTADISTICAS")
        print("========================================")
        print("1. listado general de productos")
        print("2. productos con existencias iguales o inferiores al stock minimo")
        print("3. historial de ventas")
        print("4. total de ingresos por ventas")
        print("5. producto con mayor cantidad de unidades vendidas")
        print("6. valor total del inventario disponible")
        print("7. promedio de ventas por periodo")
        print("8. regresar al menu principal")
        print("========================================")
        
        opcion = input("seleccione una opcion (1-8): ").strip()
        
        if opcion == "1":
            from productos import listar_productos
            listar_productos()
        elif opcion == "2":
            reporte_stock_minimo()
        elif opcion == "3":
            from ventas import consultar_historial_ventas
            consultar_historial_ventas()
        elif opcion == "4":
            reporte_total_ingresos()
        elif opcion == "5":
            reporte_producto_mas_vendido()
        elif opcion == "6":
            reporte_valor_inventario()
        elif opcion == "7":
            reporte_promedio_ventas()
        elif opcion == "8":
            break
        else:
            print("error: opcion invalida intente de nuevo")



def reporte_stock_minimo():
    """muestra productos con existencias iguales o inferiores al stock minimo"""
    print("\n--PRODUCTOS CON STOCK MINIMO O INFERIOR--")
    productos = cargar_datos(archivo_productos)
    
    encontrados = [p for p in productos if p["cantidad_disponible"] <= p["stock_minimo"]]
    
    if not encontrados:
        print("no hay productos en stock minimo o inferior")
        return
        
    print(f"{'codigo':<10} | {'nombre':<20} | {'disponible':<12} | {'stock min'}")
    print("-" * 55)
    for p in encontrados:
        print(f"{p['codigo']:<10} | {p['nombre']:<20} | {p['cantidad_disponible']:<12} | {p['stock_minimo']}")




def reporte_total_ingresos():
    """muestra el total de ingresos generados por las ventas"""
    print("\n--TOTAL DE INGRESOS POR VENTAS--")
    ventas = cargar_datos(archivo_ventas)
    
    if not ventas:
        print("no hay ventas registradas")
        return
        
    total_ingresos = sum(v["total"] for v in ventas)
    total_ventas_realizadas = len(ventas)
    
    print(f"numero total de ventas: {total_ventas_realizadas}")
    print(f"ingresos totales acumulados: Q{total_ingresos:.2f}")


def reporte_producto_mas_vendido():
    """identifica el producto con mayor cantidad de unidades vendidas"""
    print("\n--PRODUCTO CON MAYOR CANTIDAD DE UNIDADES VENDIDAS--")
    ventas = cargar_datos(archivo_ventas)
    
    if not ventas:
        print("no hay ventas registradas")
        return
        
    conteo_unidades = {}
    for v in ventas:
        for item in v["items"]:
            cod = item["codigo"]
            cant = item["cantidad"]
            conteo_unidades[cod] = conteo_unidades.get(cod, 0) + cant
            
    if not conteo_unidades:
        print("no hay datos suficientes")
        return
        
    codigo_top = max(conteo_unidades, key=conteo_unidades.get)
    unidades_top = conteo_unidades[codigo_top]
    
    productos = cargar_datos(archivo_productos)
    nombre_top = codigo_top
    for p in productos:
        if p["codigo"] == codigo_top:
            nombre_top = p["nombre"]
            break
            
    print(f"producto ganador: {nombre_top} (codigo: {codigo_top})")
    print(f"unidades totales vendidas: {unidades_top}")

def reporte_valor_inventario():
    """calcula el valor total del inventario disponible basado en precio de venta y cantidad"""
    print("\n--VALOR TOTAL DEL INVENTARIO DISPONIBLE--")
    productos = cargar_datos(archivo_productos)
    
    if not productos:
        print("no hay productos registrados")
        return
        
    valor_total = sum(p["cantidad_disponible"] * p["precio_venta"] for p in productos if p["activo"])
    print(f"valor total estimado del inventario activo: Q{valor_total:.2f}")




def reporte_promedio_ventas():
    """calcula el promedio de ventas por transaccion registrada"""
    print("\n--PROMEDIO DE VENTAS POR PERIODO / TRANSACCION--")
    ventas = cargar_datos(archivo_ventas)
    
    if not ventas:
        print("no hay ventas registradas")
        return
        
    total_ingresos = sum(v["total"] for v in ventas)
    cantidad_ventas = len(ventas)
    promedio = total_ingresos / cantidad_ventas
    
    print(f"total de transacciones: {cantidad_ventas}")
    print(f"promedio de venta por transaccion: Q{promedio:.2f}")


"""hola pruebaaa"""


