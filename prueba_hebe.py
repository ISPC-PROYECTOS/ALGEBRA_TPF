import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Paso 1: Leer el archivo CSV
df = pd.read_csv('ventas_simuladas.csv', delimiter=',', quotechar='"', engine='python')

# Paso 2: Ver las primeras filas del DataFrame para inspeccionar los datos
print("Primeras filas del DataFrame:")
print(df.head())

# Paso 3: Limpiar los datos

# Convertir la columna 'fecha' a tipo datetime (si hay valores incorrectos, serán NaT)
df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce')  # 'coerce' convierte a NaT los valores incorrectos

# Convertir la columna 'hora' a tipo datetime solo con la hora
df['hora'] = pd.to_datetime(df['hora'], format='%H:%M:%S', errors='coerce').dt.time

# Convertir 'precio' y 'total_venta' a tipo numérico (si hay valores no numéricos, los convertimos a NaN)
df['precio'] = pd.to_numeric(df['precio'], errors='coerce')
df['total_venta'] = pd.to_numeric(df['total_venta'], errors='coerce')

# Paso 4: Verificación de valores nulos antes de continuar con la limpieza
print("Valores nulos antes de la limpieza:")
print(df.isnull().sum())

# Paso 5: Rellenar los valores nulos para las columnas específicas
df['fecha'] = df['fecha'].ffill()  # Rellenamos las fechas faltantes con el valor anterior
df['hora'] = df['hora'].ffill()  # Rellenamos las horas faltantes con el valor anterior

# Rellenamos los valores numéricos con la media de la columna correspondiente
df['precio'] = df['precio'].fillna(df['precio'].mean())  # Rellenar con la media de la columna
df['total_venta'] = df['total_venta'].fillna(df['total_venta'].mean())  # Rellenar con la media

# Paso 6: Verificación de valores nulos después de la limpieza
print("Valores nulos después de la limpieza:")
print(df.isnull().sum())

# Paso 7: Asegurarse de que las columnas de texto estén bien formateadas
df['nombre_art'] = df['nombre_art'].astype(str)  # Asegurarse de que 'nombre_art' sea texto
df['presentacion'] = df['presentacion'].astype(str)  # Asegurarse de que 'presentacion' sea texto

# Ver las primeras filas después de la limpieza
print("\nPrimeras filas después de la limpieza:")
print(df.head())

# Paso 8: Análisis Exploratorio de los Datos
# Gráfico de las ventas totales por día
ventas_diarias = df.groupby('fecha')['total_venta'].sum()

plt.figure(figsize=(10,6))
ventas_diarias.plot(kind='line', color='blue')
plt.title('Ventas Totales por Día')
plt.xlabel('Fecha')
plt.ylabel('Total Venta')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Paso 9: Preparación de los datos para PCA
df_numeric = df[['precio', 'cantidad_art', 'total_venta']]

# Verificar si hay valores NaN antes de la normalización
print("\nValores nulos en columnas numéricas antes de la normalización:")
print(df_numeric.isnull().sum())

# Rellenar cualquier valor NaN antes de normalizar
df_numeric = df_numeric.fillna(df_numeric.mean())

# Normalizamos los datos para que todas las características tengan la misma escala
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_numeric)

# Paso 10: Aplicar PCA
pca = PCA(n_components=2)  # Reducimos a 2 dimensiones
pca_result = pca.fit_transform(df_scaled)

# Paso 11: Ver la varianza explicada por cada componente
print(f'Varianza explicada por cada componente: {pca.explained_variance_ratio_}')

# Paso 12: Crear un DataFrame con los resultados de PCA
df_pca = pd.DataFrame(data=pca_result, columns=['PC1', 'PC2'])

# Paso 13: Graficar los resultados del PCA
plt.figure(figsize=(10,6))
plt.scatter(df_pca['PC1'], df_pca['PC2'], alpha=0.5, c=df['precio'], cmap='viridis')
plt.colorbar(label='Precio')
plt.title('Análisis de Componentes Principales (PCA)')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.show()

# Paso 14: Análisis adicional - Análisis de correlaciones entre variables
correlation_matrix = df[['precio', 'cantidad_art', 'total_venta']].corr()
print("Matriz de correlación entre variables:")
print(correlation_matrix)
