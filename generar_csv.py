import random
import pandas as pd
from datetime import datetime, timedelta

# Listas de productos y presentaciones para elegir aleatoriamente
productos = ["HARINA INTEGRAL", "NUECES", "ALMOHADITAS FRUTILLA", "PIMENTON DULCE", "LENTEJAS", "QUINOA"]
presentaciones = ["1 kg", "500 g", "250 g", "300 g"]
precios = {"HARINA INTEGRAL": 2200.00, "NUECES": 300.00, "ALMOHADITAS FRUTILLA": 400.00, 
           "PIMENTON DULCE": 120.00, "LENTEJAS": 300.00, "QUINOA": 600.00}

# Función para generar una fecha aleatoria dentro de un rango de fechas
def generar_fecha_aleatoria(inicio, fin):
    delta = fin - inicio
    random_day = random.randint(0, delta.days)
    return inicio + timedelta(days=random_day)

# Función para generar hora aleatoria
def generar_hora_aleatoria():
    return f"{random.randint(0, 23):02d}.{random.randint(0, 59):02d}.00"

# Generación de datos
def generar_datos_ventas(n):
    ventas = []
    fecha_inicio = datetime(2023, 2, 1)
    fecha_fin = datetime(2023, 2, 12)

    for i in range(1, n+1):
        fecha = generar_fecha_aleatoria(fecha_inicio, fecha_fin).strftime("%Y.%m.%d")
        hora = generar_hora_aleatoria()
        cantidad_art = random.randint(1, 5)
        nombre_art = random.choice(productos)
        presentacion = random.choice(presentaciones)
        precio = precios[nombre_art]
        total_venta = cantidad_art * precio
        ventas.append([i, fecha, hora, cantidad_art, nombre_art, presentacion, precio, total_venta])
    
    # Crear un DataFrame con los datos generados
    df = pd.DataFrame(ventas, columns=["id", "fecha", "hora", "cantidad_art", "nombre_art", "presentacion", "precio", "total_venta"])
    return df

# Generar los datos de ventas
df_ventas = generar_datos_ventas(1944)

# Guardar el DataFrame a un archivo CSV
df_ventas.to_csv("ventas_diarias_prueba.csv", index=False)

# Mostrar los primeros registros generados
print(df_ventas.head())