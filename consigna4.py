import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Paso 1: Leer el archivo CSV original
df = pd.read_csv('ventas_diarias.csv', delimiter=',', quotechar='"', engine='python')

# Paso 2: Ver las primeras filas para asegurarnos de que se cargaron correctamente
print("Primeras filas del DataFrame:")
print(df.head())

# Paso 3: Aplicar una variación aleatoria del 5% a la columna 'cantidad_art'
# Usamos np.random.uniform para generar un valor aleatorio entre -5% y +5% de cada cantidad
df['cantidad_art'] = df['cantidad_art'] * (1 + np.random.uniform(-0.05, 0.05, size=len(df)))

# Paso 4: Verificar los primeros valores modificados
print("\nPrimeras filas con la variación aplicada a 'cantidad_art':")
print(df[['id', 'cantidad_art']].head())  # Solo mostramos las columnas relevantes

# Paso 5: Guardar el DataFrame modificado en un nuevo archivo CSV (respetando la estructura original)
df.to_csv('ventas_modificadas.csv', index=False)

print("\nNuevo archivo 'ventas_modificadas.csv' guardado exitosamente.")


# Gráfico de barras de ventas diarias
import matplotlib.pyplot as plt
import pandas as pd

import matplotlib.pyplot as plt
import pandas as pd

import matplotlib.pyplot as plt
import pandas as pd

def generar_grafico_barras(df):
    df['fecha'] = pd.to_datetime(df['fecha'])
    ventas_diarias = df.groupby(df['fecha'].dt.date)['total_venta'].sum()
    ventas_diarias.plot(kind='bar', figsize=(12, 6), color='skyblue')
    plt.title("Ventas diarias")
    plt.xlabel("Fecha")
    plt.ylabel("Total de venta ($)")
    fechas_mostradas = [fecha.strftime('%Y-%m-%d') for fecha in ventas_diarias.index]
    plt.xticks(range(0, len(ventas_diarias), max(1, len(ventas_diarias)//10)), fechas_mostradas[::max(1, len(ventas_diarias)//10)], rotation=45)
    plt.tight_layout()
    plt.show()

# Gráfico de dispersión de cantidad vs. total de venta
def generar_grafico_dispersion(df):
    plt.figure(figsize=(10, 6))
    plt.scatter(df['cantidad_art'], df['total_venta'], color='purple', alpha=0.5)
    plt.title("Cantidad vs. Total de venta")
    plt.xlabel("Cantidad de artículos")
    plt.ylabel("Total de venta ($)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Gráfico circular de ventas por producto
def generar_grafico_circular(df):
    ventas_por_producto = df.groupby('nombre_art')['total_venta'].sum()
    ventas_por_producto.plot(kind='pie', figsize=(8, 8), autopct='%1.1f%%')
    plt.title("Ventas por producto")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()

# Gráfico semanal de ventas por valor
def generar_grafico_semanal(df):
    df['fecha'] = pd.to_datetime(df['fecha'])
    df['semana'] = df['fecha'].dt.isocalendar().week
    ventas_semanales = df.groupby('semana')['total_venta'].sum()
    ventas_semanales.plot(kind='bar', figsize=(12, 6), color='lightgreen')
    plt.title("Ventas semanales")
    plt.xlabel("Semana")
    plt.ylabel("Total de venta ($)")
    plt.tight_layout()
    plt.show()

# Gráfico mensual de ventas por valor
def generar_grafico_mensual(df):
    df['fecha'] = pd.to_datetime(df['fecha'])
    df['mes'] = df['fecha'].dt.month
    ventas_mensuales = df.groupby('mes')['total_venta'].sum()
    ventas_mensuales.plot(kind='bar', figsize=(10, 6), color='orange')
    plt.title("Ventas mensuales")
    plt.xlabel("Mes")
    plt.ylabel("Total de venta ($)")
    plt.tight_layout()
    plt.show()

# Gráfico mensual de ventas por productos
def generar_grafico_mensual_producto(df):
    df['fecha'] = pd.to_datetime(df['fecha'])
    df['mes'] = df['fecha'].dt.month
    ventas_mensuales_producto = df.groupby(['mes', 'nombre_art'])['total_venta'].sum().unstack().fillna(0)
    ventas_mensuales_producto.plot(kind='bar', stacked=True, figsize=(12, 8))
    plt.title("Ventas mensuales por productos")
    plt.xlabel("Mes")
    plt.ylabel("Total de venta ($)")
    plt.tight_layout()
    plt.show()

# Gráfico anual de ventas por productos
def generar_grafico_anual_producto(df):
    df['fecha'] = pd.to_datetime(df['fecha'])
    df['anio'] = df['fecha'].dt.year
    ventas_anuales_producto = df.groupby(['anio', 'nombre_art'])['total_venta'].sum().unstack().fillna(0)
    ventas_anuales_producto.plot(kind='bar', stacked=True, figsize=(12, 8))
    plt.title("Ventas anuales por productos")
    plt.xlabel("Año")
    plt.ylabel("Total de venta ($)")
    plt.tight_layout()
    plt.show()

# Gráfico circular de monto de ventas por producto
def generar_grafico_circular_monto_por_producto(df):
    ventas_por_producto = df.groupby('nombre_art')['total_venta'].sum()
    ventas_por_producto.plot(kind='pie', figsize=(8, 8), autopct='%1.1f%%', startangle=90, shadow=True)
    plt.title("Monto de ventas por producto")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()

# Gráfico promedio de ventas por hora
def generar_grafico_promedio_ventas_horas(df):
    df['hora'] = pd.to_datetime(df['hora'], format='%H.%M.%S').dt.hour
    ventas_horarias = df.groupby('hora')['total_venta'].mean()
    ventas_horarias.plot(kind='line', marker='o', color='blue', figsize=(10, 6))
    plt.title("Promedio de ventas por hora")
    plt.xlabel("Hora")
    plt.ylabel("Promedio de venta ($)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

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
   
    if df is None:
        print("No se pudo cargar los datos. Asegúrate de que el archivo existe.")
        return
    
    salir = False
    while not salir:
        print("\n---> MENÚ DE OPCIONES <---")
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
        elif opcion == '9':
            generar_grafico_circular_monto_por_producto(df)
        elif opcion == '10':
            generar_grafico_promedio_ventas_horas(df)
        elif opcion == '11':
            generar_grafico_proyeccion_anual_producto(df)
        elif opcion == '12':
            salir = True
        else: 
            print('Opción incorrecta.')

if __name__ == '__main__':
    menu_ventas_diarias()