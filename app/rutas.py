from flask import Blueprint, render_template
from .modelos import obtener_analisis_ventas
import pandas as pd
import matplotlib.pyplot as plt
import os  # Importa el módulo os
from .db_conexion import db
import numpy as np

app = Blueprint('app', __name__)

@app.route('/')
def dashboard():
    # Obtener análisis de ventas
    analisis = obtener_analisis_ventas()
    
    # Convertir datos a DataFrame
    df = pd.DataFrame(list(db.VentasBicicleta.find()))  # Cambiado de db.db a db

    # Convertir columnas a tipos adecuados
    df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')  # Asegura que 'Quantity' sea numérico
    df['Customer_Age'] = pd.to_numeric(df['Customer_Age'], errors='coerce')  # Asegura que 'Customer_Age' sea numérico
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')  # Asegura que 'Price' sea numérico

    # Eliminar filas con valores NaN en las columnas críticas
    df = df.dropna(subset=['Quantity', 'Customer_Age', 'Price'])

    # Realizar análisis y graficar
    graficar_ventas_por_ciudad(df)
    graficar_cantidad_por_modelo(df)
    graficar_distribucion_edad(df)
    graficar_metodo_pago(df)
    graficar_edad_por_modelo(df)
    graficar_precio_por_modelo(df)
    graficar_ubicacion_por_modelo(df)
    graficar_metodo_pago_por_edad(df)
    graficar_metodo_pago(df)
    graficar_edad_vs_modelo(df)
    graficar_metodo_pago_por_ubicacion(df)


    # Pasar los análisis a la plantilla
    return render_template('dashboard.html', analisis=analisis)

def graficar_ventas_por_ciudad(df):
    """Grafica las ventas por ciudad y guarda la imagen en static/img."""
    os.makedirs('static/img', exist_ok=True)
    ventas_por_ciudad = df.groupby('Store_Location')['Quantity'].sum()
    plt.figure(figsize=(10, 6))
    ventas_por_ciudad.plot(kind='bar', color='skyblue')
    plt.title('Ventas por Ciudad')
    plt.xlabel('Ciudad')
    plt.ylabel('Cantidad de Ventas')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/img/ventas_por_ciudad.png')  # Guarda la imagen
    plt.close()

def graficar_cantidad_por_modelo(df):
    """Grafica la cantidad vendida por modelo de bicicleta y guarda la imagen en static/img."""
    os.makedirs('static/img', exist_ok=True)
    cantidad_por_modelo = df.groupby('Bike_Model')['Quantity'].sum()
    plt.figure(figsize=(10, 6))
    cantidad_por_modelo.plot(kind='bar', color='lightgreen')
    plt.title('Cantidad Vendida por Modelo de Bicicleta')
    plt.xlabel('Modelo de Bicicleta')
    plt.ylabel('Cantidad Vendida')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/img/cantidad_por_modelo.png')  # Guarda la imagen
    plt.close()

def graficar_distribucion_edad(df):
    """Grafica la distribución de edad de los compradores y guarda la imagen en static/img."""
    os.makedirs('static/img', exist_ok=True)
    plt.figure(figsize=(10, 6))
    plt.hist(df['Customer_Age'], bins=20, color='salmon', edgecolor='black')
    plt.title('Distribución de Edad de los Compradores')
    plt.xlabel('Edad')
    plt.ylabel('Frecuencia')
    plt.grid(axis='y')
    plt.tight_layout()
    plt.savefig('static/img/distribucion_edad.png')  # Guarda la imagen
    plt.close()

def graficar_metodo_pago(df):
    """Grafica el método de pago utilizado y guarda la imagen en static/img."""
    os.makedirs('static/img', exist_ok=True)
    metodo_pago_counts = df['Payment_Method'].value_counts()
    plt.figure(figsize=(10, 6))
    metodo_pago_counts.plot(kind='bar', color='lightcoral')
    plt.title('Método de Pago Utilizado')
    plt.xlabel('Método de Pago')
    plt.ylabel('Cantidad de Ventas')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/img/metodo_pago.png')  # Guarda la imagen
    plt.close()

def graficar_edad_por_modelo(df):
    """Grafica la edad de los compradores por modelo de bicicleta y guarda la imagen en static/img."""
    os.makedirs('static/img', exist_ok=True)
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Bike_Model'], df['Customer_Age'], alpha=0.5, color='purple')
    plt.title('Edad de los Compradores por Modelo de Bicicleta')
    plt.xlabel('Modelo de Bicicleta')
    plt.ylabel('Edad')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/img/edad_por_modelo.png')  # Guarda la imagen
    plt.close()

def graficar_precio_por_modelo(df):
    """Grafica el precio por modelo de bicicleta y guarda la imagen en static/img."""
    os.makedirs('static/img', exist_ok=True)
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Bike_Model'], df['Price'], alpha=0.5, color='orange')
    plt.title('Precio por Modelo de Bicicleta')
    plt.xlabel('Modelo de Bicicleta')
    plt.ylabel('Precio')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/img/precio_por_modelo.png')  # Guarda la imagen
    plt.close()

def graficar_ubicacion_por_modelo(df):
    """Grafica la ubicación de ventas por modelo de bicicleta y guarda la imagen en static/img."""
    os.makedirs('static/img', exist_ok=True)
    ubicacion_counts = df.groupby(['Bike_Model', 'Store_Location']).size().unstack(fill_value=0)
    ubicacion_counts.plot(kind='bar', stacked=True, figsize=(10, 6))
    plt.title('Ubicación de Ventas por Modelo de Bicicleta')
    plt.xlabel('Modelo de Bicicleta')
    plt.ylabel('Cantidad de Ventas')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/img/ubicacion_por_modelo.png')  # Guarda la imagen
    plt.close()

def graficar_metodo_pago_por_edad(df):
    """Grafica el método de pago por edad de compradores y guarda la imagen en static/img."""
    os.makedirs('static/img', exist_ok=True)
    plt.figure(figsize=(10, 6))
    # Agrupando y contando el método de pago por edad
    metodo_pago_por_edad = df.groupby('Customer_Age')['Payment_Method'].value_counts().unstack()
    metodo_pago_por_edad.plot(kind='bar', stacked=True, figsize=(10, 6))
    plt.title('Método de Pago por Edad de Compradores')
    plt.xlabel('Edad')
    plt.ylabel('Frecuencia')
    plt.grid(axis='y')
    plt.tight_layout()
    plt.savefig('static/img/metodo_pago_por_edad.png')  # Guarda la imagen
    plt.close()

def graficar_metodo_pago(df):
    """Grafica el método de pago y guarda la imagen en static/img."""
    os.makedirs('static/img', exist_ok=True)

    metodo_pago = df.groupby('Payment_Method')['Quantity'].sum()
    plt.figure(figsize=(10, 6))
    metodo_pago.plot(kind='bar', color='orange')
    plt.title('Método de Pago Favorito')
    plt.xlabel('Método de Pago')
    plt.ylabel('Cantidad de Ventas')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/img/metodo_pago_favorito.png')
    plt.close()

def graficar_edad_vs_modelo(df):
    """Grafica edad vs modelo y guarda la imagen en static/img."""
    os.makedirs('static/img', exist_ok=True)
    edad_promedio_por_modelo = df.groupby('Bike_Model')['Customer_Age'].mean().reset_index()
    plt.figure(figsize=(10, 6))
    bars =plt.bar(edad_promedio_por_modelo['Bike_Model'], edad_promedio_por_modelo['Customer_Age'], color = 'purple', alpha = 0.7)
    z = np.polyfit(range(len(edad_promedio_por_modelo)), edad_promedio_por_modelo['Customer_Age'],1)
    p = np.poly1d(z)
    plt.plot(edad_promedio_por_modelo['Bike_Model'],p(range(len(edad_promedio_por_modelo))),color = 'orange', linestyle = '--', label = 'Tendencia')
    plt.title('Edad Promedio vs Modelo de Bicicleta')
    plt.xlabel('Modelo Bicicleta')
    plt.ylabel('Edad Promedio')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig('static/img/edad_vs_modelo.png')
    plt.close()


def graficar_metodo_pago_por_ubicacion(df):
    """Grafica el método de pago por ubicación y guarda la imagen en static/img."""
    os.makedirs('static/img', exist_ok=True)
    metodo_pago_por_ubicacion = df.groupby(['Store_Location', 'Payment_Method']).size().unstack(fill_value=0)
    metodo_pago_por_ubicacion.plot(kind='bar', stacked=True, figsize=(10, 6))
    plt.title('Método de Pago por Ubicación')
    plt.xlabel('Ubicación')
    plt.ylabel('Cantidad de Ventas')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/img/metodo_pago_por_ubicacion.png')  # Guarda la imagen
    plt.close()
