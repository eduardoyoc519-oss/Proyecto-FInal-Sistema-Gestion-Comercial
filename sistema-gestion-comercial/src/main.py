
# MENU PRINCIPAL DEL SISTEMA (main.py


from productos import (
    registrar_producto,
    consultar_producto_por_codigo,
    listar_productos,
    modificar_producto,
    desactivar_producto
)
from ventas import registrar_venta, consultar_historial_ventas
from inventario import (
    consultar_existencias,
    registrar_entrada_inventario,
    consultar_historial_movimientos
)
from reportes import generar_reportes_menu


def mostrar_menu():
    """muestra las opciones del menu principal"""
    while True:
        print("\n========================================")
        print("     SISTEMA DE GESTION COMERCIAL")
        print("========================================")
        print("1. modulo de gestion de productos")
        print("2. modulo de registro de ventas")
        print("3. modulo de control de inventarios")
        print("4. modulo de reportes y estadisticas")
        print("5. salir del sistema")
        print("========================================")
        
        opcion = input("ingrese una opcion del menu (1-5): ").strip()
        
        if opcion == "1":
            menu_productos()
        elif opcion == "2":
            menu_ventas()
        elif opcion == "3":
            menu_inventario()
        elif opcion == "4":
            generar_reportes_menu()
        elif opcion == "5":
            print("\nsaliendo del sistema de gestion comercial")
            break
        else:
            print("error: opcion invalida por favor seleccione un numero entre 1 y 5")



def menu_productos():
    """sub-menu para la gestion de productos"""
    while True:
        print("\n--- MENU GESTION DE PRODUCTOS ---")
        print("1. registrar nuevo producto")
        print("2. consultar producto por codigo")
        print("3. listar todos los productos")
        print("4. modificar informacion de producto")
        print("5. desactivar producto")
        print("6. regresar al menu principal")
        
        opcion = input("seleccione una opcion (1-6): ").strip()
        
        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            consultar_producto_por_codigo()
        elif opcion == "3":
            listar_productos()
        elif opcion == "4":
            modificar_producto()
        elif opcion == "5":
            desactivar_producto()
        elif opcion == "6":
            break
        else:
            print("error: opcion invalida")

def menu_ventas():
    """sub-menu para el registro de ventas"""
    while True:
        print("\n--- MENU REGISTRO DE VENTAS ---")
        print("1. registrar nueva venta")
        print("2. consultar historial de ventas")
        print("3. regresar al menu principal")
        
        opcion = input("seleccione una opcion (1-3): ").strip()
        
        if opcion == "1":
            registrar_venta()
        elif opcion == "2":
            consultar_historial_ventas()
        elif opcion == "3":
            break
        else:
            print("error: opcion invalida")


def menu_inventario():
    """sub-menu para el control de inventarios"""
    while True:
        print("\n--- MENU CONTROL DE INVENTARIOS ---")
        print("1. consultar existencias actuales")
        print("2. registrar entrada de inventario")
        print("3. consultar historial de movimientos")
        print("4. regresar al menu principal")
        
        opcion = input("seleccione una opcion (1-4): ").strip()
        
        if opcion == "1":
            consultar_existencias()
        elif opcion == "2":
            registrar_entrada_inventario()
        elif opcion == "3":
            consultar_historial_movimientos()
        elif opcion == "4":
            break
        else:
            print("error: opcion invalida")


if __name__ == "__main__":
    mostrar_menu()



