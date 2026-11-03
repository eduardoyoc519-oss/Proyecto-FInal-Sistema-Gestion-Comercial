# MANUAL TECNICO - SISTEMA DE GESTION COMERCIAL

## 1. Proposito del Sistema
Brindar una solución de consola basada en Python para el control de inventarios registro de ventas y emisión de reportes comerciales utilizando almacenamiento local en JSON

## 2. Arquitectura y Módulos
El sistema está estructurado modularmente:
- **archivos.py**: Gestiona la persistencia de datos con `json` y `os`
- **productos.py**: ABCC (altas, bajas, consultas y cambios) de productos
- **ventas.py**: Gestión de carrito, cálculo de subtotales, IVA (12%) y rebaja de stock
- **inventario.py**: Entradas de mercadería y bitácora de movimientos
- **reportes.py**: Estadísticas e indicadores financieros
- **main.py**: Orquestador principal mediante bucles y menús interactivos

## 3. Requisitos del Sistema
- Interprete de Python 3.8 o superior
- Permisos de lectura y escritura en la carpeta local para la creación automática del directorio `data/`



