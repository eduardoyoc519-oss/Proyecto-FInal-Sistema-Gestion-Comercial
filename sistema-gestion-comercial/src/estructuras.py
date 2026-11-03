
# MODULO DE ESTRUCTURAS DE DATOS (estructuras.py)

# estructuras base y diccionarios "sistema"
 

def estructura_producto(codigo, nombre, categoria, precio, cantidad, stock_minimo):
    """define la estructura de datos para un producto nuevo"""
    return {
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "precio_venta": float(precio),
        "cantidad_disponible": int(cantidad),
        "stock_minimo": int(stock_minimo),
        "activo": True
    }


def estructura_venta(numero_venta, fecha, items, subtotal, iva, total):
    """define la estructura de datos para una transaccion de venta"""
    return {
        "numero_venta": numero_venta,
        "fecha": fecha,
        "items": items,
        "subtotal": float(subtotal),
        "iva": float(iva),
        "total": float(total)
    }



def estructura_movimiento(fecha, codigo, tipo, cantidad, descripcion):
    """define la estructura de datos para el historial de inventario"""
    return {
        "fecha": fecha,
        "codigo": codigo,
        "tipo": tipo,
        "cantidad": int(cantidad),
        "descripcion": descripcion
    }


