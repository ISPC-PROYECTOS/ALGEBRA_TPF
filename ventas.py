import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def cargar_datos_ventas(archivo_ventas="ventas_diarias.csv"):
    try:
        df = pd.read_csv(archivo_ventas)
        print(f"Datos cargados de {archivo_ventas}.")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo_ventas}.")
        return None
    return df

# Función para proyectar ventas anuales por producto mediante regresión lineal
def generar_grafico_proyeccion_anual_producto(df):
    df['fecha'] = pd.to_datetime(df['fecha'])
    df['anio'] = df['fecha'].dt.year
    df['mes'] = df['fecha'].dt.month
    
    # Agrupación de datos de ventas por mes y producto
    ventas_mensuales_producto = df.groupby(['anio', 'mes', 'nombre_art'])['total_venta'].sum().unstack().fillna(0)

    plt.figure(figsize=(12, 8))

    # Generación de la regresión y proyección para cada producto
    for producto in ventas_mensuales_producto.columns:
        # Extrae las ventas del producto y prepara datos para la regresión
        ventas = ventas_mensuales_producto[producto]
        x = np.arange(len(ventas))  # Meses como números
        y = ventas.values

        # Cálculo de la regresión lineal
        slope, intercept, r_value, p_value, std_err = linregress(x, y)

        # Proyección de ventas futuras para el próximo año
        x_future = np.arange(len(ventas) + 12)  # Extiende 12 meses (1 año) hacia el futuro
        y_future = intercept + slope * x_future

        # Grafica las ventas pasadas y la proyección
        plt.plot(x, y, label=f"{producto} - Ventas pasadas")
        plt.plot(x_future, y_future, '--', label=f"{producto} - Proyección", alpha=0.7)

    # Cálculo dinámico de etiquetas de meses en el eje x
    total_meses = len(x_future)
    etiquetas_meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'] * (total_meses // 12 + 1)

    plt.title("Proyección anual de ventas por producto mediante regresión lineal")
    plt.xlabel("Mes")
    plt.ylabel("Total de venta ($)")
    plt.xticks(np.arange(total_meses), labels=etiquetas_meses[:total_meses], rotation=45)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.tight_layout()
    plt.show()

# Código del menú para incluir la nueva función de proyección
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
        print("11. Gráfico de proyección anual de ventas por producto")
        print("12. Salir")
        
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
            generar_grafico_proyeccion_anual_producto(df)
        elif opcion == "12":
            print("Saliendo de ventas diarias.")
            salir = True
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == '__main__':
    menu_ventas_diarias()
