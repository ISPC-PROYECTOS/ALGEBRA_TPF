import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Establecer semilla para resultados reproducibles
np.random.seed(42)

# Definir los productos y sus precios
productos = {
    'HARINA INTEGRAL': ['500 g', '1 kg'],
    'LENTEJAS': ['1 kg', '250 g'],
    'ALMOHADITAS FRUTILLA': ['250 g', '300 g'],
    'NUECES': ['250 g', '300 g', '500 g'],
    'QUINOA': ['500 g', '1 kg'],
    'PIMENTON DULCE': ['250 g', '500 g']
}

# Precios por unidad de cada producto (el precio depende del producto, no de la presentación)
precios = {
    'HARINA INTEGRAL': 2200.00,
    'LENTEJAS': 300.00,
    'ALMOHADITAS FRUTILLA': 400.00,
    'NUECES': 300.00,
    'QUINOA': 600.00,
    'PIMENTON DULCE': 120.00
}

# Definir el rango de fechas para seis meses (1 febrero 2023 a 31 julio 2023)
fechas = pd.date_range(start='2024-07-01', end='2024-11-10', freq='D')

# Generar ventas diarias aleatorias para los seis meses
insert_queries = []

for fecha in fechas:
    for _ in range(3):  # Generar 3 ventas por día
        # Generar una hora aleatoria entre 08:00 y 20:59 (de 8 AM a 8:59 PM)
        hora = f'{random.randint(8, 20):02d}:{random.randint(0, 59):02d}:00'
        
        # Seleccionar producto aleatorio
        nombre_producto = random.choice(list(productos.keys()))
        
        # Seleccionar presentación válida para el producto
        presentacion = random.choice(productos[nombre_producto])
        
        # Calcular el precio de acuerdo con el producto
        precio = precios[nombre_producto]
        
        # Generar cantidad aleatoria de productos (de 1 a 5 unidades)
        cantidad_producto = random.randint(1, 5)
        
        # Calcular el total de la venta
        total_venta = cantidad_producto * precio
        
        # Crear el comando SQL INSERT
        query = f"""
        INSERT INTO ventas_diarias (fecha, hora, cantidad_art, nombre_art, presentacion, precio, total_venta)
        VALUES ('{fecha.strftime('%Y-%m-%d')}', '{hora}', {cantidad_producto}, '{nombre_producto}', '{presentacion}', {precio:.2f}, {total_venta:.2f});
        """
        insert_queries.append(query)

# Guardar los comandos INSERT en un archivo .sql para el rango de fechas solicitado (febrero a julio 2023)
with open('ventas_diarias_insert_feb_jul_2023.sql', 'w') as file:
    for query in insert_queries:
        file.write(query + '\n')

print("Comandos INSERT generados y guardados en 'ventas_diarias_insert_feb_jul_2023.sql'.")
