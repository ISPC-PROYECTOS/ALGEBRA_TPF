import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Establecer semilla para resultados reproducibles
random.seed(42)

# Definir los productos y sus precios
productos = ['HARINA INTEGRAL', 'LENTEJAS', 'ALMOHADITAS FRUTILLA', 'NUECES', 'QUINOA', 'PIMENTON DULCE']
presentaciones = ['500 g', '1 kg', '250 g', '300 g', '500 ml', '1 L']
precios = {'HARINA INTEGRAL': 2200.00, 'LENTEJAS': 300.00, 'ALMOHADITAS FRUTILLA': 400, 
           'NUECES': 300.00, 'QUINOA': 600.00, 'PIMENTON DULCE': 120.00}

# Generar fechas de ejemplo (de febrero de 2023)
fechas = pd.date_range(start='2023-02-01', end='2023-02-05', freq='D')

# Crear lista para almacenar los registros
datos = []

# Generar datos aleatorios
for i in range(1, 31):  # 30 registros para simular 5 días de ventas
    for fecha in fechas:
        # Generar hora aleatoria entre 08:00 y 20:00
        hora = f'{random.randint(8, 20)}:{random.randint(0, 59):02d}:00'
        
        # Seleccionar producto, cantidad y presentación
        nombre_producto = random.choice(productos)
        cantidad_producto = random.randint(1, 5)
        presentacion = random.choice(presentaciones)
        precio = precios[nombre_producto]
        
        # Calcular el total de la venta
        total_venta = cantidad_producto * precio
        
        # Crear el registro
        registro = {
            'id': i,
            'fecha': fecha.strftime('%Y-%m-%d'),
            'hora': hora,
            'cantidad_art': cantidad_producto,
            'nombre_art': nombre_producto,
            'presentacion': presentacion,
            'precio': precio,
            'total_venta': total_venta
        }
        
        # Agregar a la lista de datos
        datos.append(registro)

# Crear DataFrame de Pandas con los datos generados
df = pd.DataFrame(datos)

# Guardar el DataFrame en un archivo CSV
df.to_csv('ventas_simuladas.csv', index=False)

print("Archivo CSV 'ventas_simuladas.csv' generado correctamente.")
