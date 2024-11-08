import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def cargar_datos_ventas(archivo_ventas="ventas_diarias.csv"):
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

def generar_grafico_semanal(df):
    df['fecha'] = pd.to_datetime(df['fecha'])
    df['semana'] = df['fecha'].dt.isocalendar().week
    
    ventas_semanales = df.groupby('semana')['total_venta'].sum()

    plt.figure(figsize=(10, 6))
    plt.bar(ventas_semanales.index, ventas_semanales.values, color='green')
    plt.title("Ventas semanales por valor")
    plt.xlabel("Semana")
    plt.ylabel("Total de venta ($)")
    plt.tight_layout()
    plt.show()

def generar_grafico_mensual(df):
    df['fecha'] = pd.to_datetime(df['fecha'])
    df['mes'] = df['fecha'].dt.month
    
    ventas_mensuales = df.groupby('mes')['total_venta'].sum()

    plt.figure(figsize=(10, 6))
    plt.bar(ventas_mensuales.index, ventas_mensuales.values, color='blue')
    plt.title("Ventas mensuales por valor")
    plt.xlabel("Mes")
    plt.ylabel("Total de venta ($)")
    plt.xticks(np.arange(1, 13), labels=['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'])
    plt.tight_layout()
    plt.show()

def generar_grafico_mensual_producto(df):
    df['fecha'] = pd.to_datetime(df['fecha'])
    df['mes'] = df['fecha'].dt.month
    
    ventas_mensuales_producto = df.groupby(['mes', 'nombre_art'])['total_venta'].sum().unstack().fillna(0)

    ventas_mensuales_producto.plot(kind='bar', stacked=True, figsize=(10, 6))
    plt.title("Ventas mensuales por productos")
    plt.xlabel("Mes")
    plt.ylabel("Total de venta ($)")
    plt.xticks(np.arange(0, 12), labels=['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'])
    plt.tight_layout()
    plt.show()

def generar_grafico_anual_producto(df):
    df['fecha'] = pd.to_datetime(df['fecha'])
    df['anio'] = df['fecha'].dt.year
    df['mes'] = df['fecha'].dt.month
    
    ventas_anuales_producto = df.groupby(['anio', 'mes', 'nombre_art'])['total_venta'].sum().unstack().fillna(0)
    
    ventas_anuales_producto.plot(kind='line', figsize=(10, 6))
    plt.title("Ventas anuales por producto por mes")
    plt.xlabel("Mes")
    plt.ylabel("Total de venta ($)")
    plt.xticks(np.arange(0, 12), labels=['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'])
    plt.tight_layout()
    plt.show()

def generar_grafico_circular_monto_por_producto(df):
    ventas_por_producto = df.groupby("nombre_art")["total_venta"].sum()
    
    plt.figure(figsize=(8, 8))
    plt.pie(ventas_por_producto, labels=ventas_por_producto.index, autopct='%1.1f%%', startangle=140)
    plt.title("Distribución de monto de ventas por producto")
    plt.axis("equal")
    plt.tight_layout()
    plt.show()

def generar_grafico_promedio_ventas_horas(df):
    # Reemplaza los puntos por dos puntos en la columna 'hora'
    df['hora'] = df['hora'].str.replace('.', ':', regex=False)
    df['hora'] = pd.to_datetime(df['hora'], format='%H:%M:%S').dt.hour
    
    # Calcula el promedio de ventas por cada hora
    promedio_ventas_por_hora = df.groupby('hora')['total_venta'].mean()
    
    # Gráfico de barras del promedio de ventas por hora
    plt.figure(figsize=(10, 6))
    plt.bar(promedio_ventas_por_hora.index, promedio_ventas_por_hora.values, color='purple')
    plt.title("Promedio de ventas por hora del día")
    plt.xlabel("Hora")
    plt.ylabel("Promedio de venta ($)")
    plt.xticks(np.arange(0, 24), rotation=45)
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
        print("5. Gráfico semanal de ventas por valor")
        print("6. Gráfico mensual de ventas por valor")
        print("7. Gráfico mensual de ventas por productos")
        print("8. Gráfico anual de ventas por productos")
        print("9. Gráfico circular de monto de ventas por producto")
        print("10. Gráfico promedio de ventas por hora")
        print("11. Salir")
        
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
            generar_grafico_semanal(df)
        elif opcion == "6":
            generar_grafico_mensual(df)
        elif opcion == "7":
            generar_grafico_mensual_producto(df)
        elif opcion == "8":
            generar_grafico_anual_producto(df)
        elif opcion == "9":
            generar_grafico_circular_monto_por_producto(df)
        elif opcion == "10":
            generar_grafico_promedio_ventas_horas(df)
        elif opcion == "11":
            print("Saliendo de ventas diarias.")
            salir = True
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == '__main__':
    menu_ventas_diarias()
