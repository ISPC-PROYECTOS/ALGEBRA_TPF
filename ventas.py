import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def cargar_datos_ventas(archivo_ventas="ventas_diarias.csv"):
    # Lee el archivo de ventas
    try:
        df = pd.read_csv(archivo_ventas)
        print(f"Datos cargados de {archivo_ventas}.")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo_ventas}.")
        return None
    return df

def generar_grafico_barras(df):
    ventas_diarias = df.groupby("fecha")["total_venta"].sum()
    
    plt.figure(figsize=(10, 6))
    plt.bar(ventas_diarias.index, ventas_diarias.values, color='skyblue')
    plt.title("Total de ventas diarias")
    plt.xlabel("Fecha")
    plt.ylabel("Total de venta ($)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def generar_grafico_circular(df):
    ventas_por_producto = df.groupby("nombre_art")["total_venta"].sum()
    
    plt.figure(figsize=(8, 8))
    plt.pie(ventas_por_producto, labels=ventas_por_producto.index, autopct='%1.1f%%', startangle=140)
    plt.title("Distribución de ventas por producto")
    plt.axis("equal")
    plt.tight_layout()
    plt.show()

def generar_grafico_dispersion(df):
    plt.figure(figsize=(10, 6))
    plt.scatter(df["cantidad_art"], df["total_venta"], color='orange')
    plt.title("Dispersión de cantidad vs. total de venta")
    plt.xlabel("Cantidad de artículos")
    plt.ylabel("Total de venta ($)")
    plt.grid()
    plt.tight_layout()
    plt.show()

def menu_ventas_diarias():
    df = cargar_datos_ventas()
    if df is None:
        print("No se pudo cargar los datos. Asegúrate de que el archivo existe.")
        return
    
    salir = False
    while not salir:
        print("\n---> MENÚ VENTAS DIARIAS <---")
        print("1. Mostrar registros de ventas")
        print("2. Gráfico de barras de ventas diarias")
        print("3. Gráfico de dispersión cantidad vs. total de venta")
        print("4. Gráfico circular de ventas por producto")
        print("5. Salir")
        
        opcion = input("Ingrese la opción que desea ejecutar: ")
        
        if opcion == "1":
            print(df)
        elif opcion == "2":
            generar_grafico_barras(df)
        elif opcion == "3":
            generar_grafico_dispersion(df)
        elif opcion == "4":
            generar_grafico_circular(df)
        elif opcion == "5":
            print("Saliendo de ventas diarias.")
            salir = True
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == '__main__':
    menu_ventas_diarias()
