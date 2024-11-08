import os
import numpy as np  
import pandas as pd  
import matplotlib.pyplot as plt  
from sklearn.decomposition import PCA  
from sklearn.preprocessing import StandardScaler  

# Cargar el archivo de ventas
def cargar_datos_ventas(archivo_ventas="ventas_diarias.csv"):
    # Verificar si el archivo existe en el directorio
    if os.path.exists(archivo_ventas):
        df = pd.read_csv(archivo_ventas)
        print(f"Datos cargados de {archivo_ventas}.")
        return df
    else:
        print(f"Error: No se encontró el archivo {archivo_ventas}. Asegúrate de que el archivo esté en el directorio correcto.")
        return None

# Función para aplicar PCA y graficar los resultados
def aplicar_pca_y_visualizar(df):
    # Seleccionar columnas numéricas para PCA
    columnas_para_pca = ['cantidad_art', 'precio', 'total_venta']  # Modificar según el archivo
    X = df[columnas_para_pca]

    # Estandarizar los datos
    scaler = StandardScaler()  
    X_scaled = scaler.fit_transform(X)  

    # Aplicar PCA
    pca = PCA(n_components=2)  # Reducir a 2 dimensiones  
    X_pca = pca.fit_transform(X_scaled)  

    # Crear un DataFrame para facilitar la visualización
    df_pca = pd.DataFrame(data=X_pca, columns=['Componente 1', 'Componente 2'])
    df_pca['Clase'] = df['nombre_art']  # Agrega la columna de productos como clase
    
    # Visualizar los resultados
    plt.figure(figsize=(10, 8))
    for clase in np.unique(df_pca['Clase']):
        plt.scatter(df_pca[df_pca['Clase'] == clase]['Componente 1'],  
                    df_pca[df_pca['Clase'] == clase]['Componente 2'],  
                    label=clase)

    plt.title('PCA de ventas diarias')
    plt.xlabel('Componente 1')
    plt.ylabel('Componente 2')
    plt.legend()
    plt.grid()
    plt.show()

# Cargar los datos y aplicar PCA
archivo = "ventas_diarias.csv"  # Asegúrate de que este archivo esté en el mismo directorio
df_ventas = cargar_datos_ventas(archivo)
if df_ventas is not None:
    aplicar_pca_y_visualizar(df_ventas)
