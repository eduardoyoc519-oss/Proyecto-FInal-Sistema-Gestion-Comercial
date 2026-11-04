# ANALISIS DETALLADO DE PROCESOS - SISTEMA COMERCIAL

## 1. Registro de Productos
* **Nombre del proceso:** Alta de Productos
* **Objetivo:** Registrar nuevos artículos en el catálogo del sistema
* **Descripción:** Permite ingresar los datos iniciales de un producto validando su unicidad
* **Datos de entrada:** Código único, Nombre, Categoría, Precio de venta, Cantidad disponible, Stock mínimo
* **Procesamiento:** Validar que el código no exista previamente en el sistema y que los valores numéricos sean positivos. Almacenar en la estructura de datos
* **Datos de salida:** Mensaje de éxito y actualización del archivo `productos.json`
* **Reglas de negocio:** Prohibido registrar códigos duplicados, precios negativos o cantidades menores a cero
* **Validaciones y errores:** Uso de bloques `try-except` para evitar caídas si se ingresan letras en campos numéricos

## 2. Consulta y Modificación de Productos
* **Nombre del proceso:** Gestión y Actualización del Catálogo
* **Objetivo:** Buscar artículos existentes y modificar sus propiedades o desactivarlos
* **Descripción:** Permite al usuario buscar por código para ver detalles o actualizar precios y stock
* **Datos de entrada:** Código de busqueda, nuevos valores a modificar
* **Procesamiento:** Recorrer la lista de productos, localizar la coincidencia por código y actualizar los campos requeridos en la memoria y en el archivo JSON
* **Datos de salida:** Ficha del producto en pantalla y confirmación de actualizacion
* **Reglas de negocio:** El código del producto no se puede modificar para mantener la integridad referencial
* **Validaciones y errores:** Mensaje de "Producto no encontrado" si el código no existe

## 3. Registro de Ventas
* **Nombre del proceso:** Facturación y Transacción Comercial
* **Objetivo:** Registrar salidas de mercancía calculando subtotales, impuestos y totales
* **Descripción:** Solicita productos y cantidades deseadas, validando existencias antes de facturar
* **Datos de entrada:** Código del producto y cantidad a vender
* **Procesamiento:** Verificar existencia, comprobar stock suficiente, calcular subtotal, calcular el **12% de IVA**, obtener el total general, restar existencias y guardar en `ventas.json`
* **Datos de salida:** Resumen de venta en consola y registro persistente
* **Reglas de negocio:** No se puede vender una cantidad mayor al stock actual disponible
* **Validaciones y errores:** Alerta de stock insuficiente o producto inexistente

## 4. Actualización de Inventario
* **Nombre del proceso:** Control de Stock y Entradas
* **Objetivo:** Monitorear existencias y registrar entradas de mercadería
* **Descripción:** Permite reabastecer productos y verificar alertas de stock crítico
* **Datos de entrada:** Código de producto y cantidad de entrada
* **Procesamiento:** Sumar la cantidad ingresada al stock actual del producto y evaluar si supera el límite de stock mínimo
* **Datos de salida:** Actualización del inventario y generación de alertas visuales
* **Reglas de negocio:** Las entradas de inventario deben sumar estrictamente valores positivos
* **Validaciones y errores:** Control de entradas inválidas o ceros

## 5. Lectura de Archivos (Persistencia)
* **Nombre del proceso:** Gestión de Archivos JSON
* **Objetivo:** Cargar y guardar la información de forma local sin base de datos externa
* **Descripción:** Utiliza la librería `json` de Python para leer y escribir en la carpeta `data/`
* **Datos de entrada:** Archivos `productos.json`, `inventario.json`, `ventas.json`
* **Procesamiento:** Apertura segura de archivos mediante sentencias `with open()`, codificación UTF-8, y serialización/deserialización con `json.load()` y `json.dump()`
* **Datos de salida:** Estructuras de datos listas para usarse en Python
* **Reglas de negocio:** Los archivos deben mantener una estructura sintáctica JSON válida
* **Validaciones y errores:** Manejo de excepciones si los archivos están vacíos o corruptos al iniciar

## 6. Generación de Reportes
* **Nombre del proceso:** Estadísticas e Informes Comerciales
* **Objetivo:** Procesar información acumulada para mostrar métricas del negocio
* **Descripción:** Calcula totales, ingresos, stock mínimo y productos más vendidos a partir de los datos reales
* **Datos de entrada:** Datos históricos de ventas y productos
* **Procesamiento:** Recorrer listas, aplicar filtros de stock mínimo, sumar ingresos totales y ordenar por unidades vendidas
* **Datos de salida:** Listados estadísticos impresos en consola
* **Reglas de negocio:** Los reportes se calculan dinámicamente de los datos almacenados, no de valores fijos
* **Validaciones y errores:** Mensaje de advertencia si no existen registros previos de ventas


