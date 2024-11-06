from pymongo import MongoClient
import pandas as pd
from flask import Flask

client = MongoClient('mongodb://localhost:27017/')
db = client['dbReporteBicicleta']
collection = db['VentasBicicleta']
data = list(collection.find({}))
    
   
def obtener_datos():
    data = list(collection.find({}))
    
    # Verifica cuántos registros se cargaron
    print(f"Registros cargados: {len(data)}")
    if data:
        print("Primeros registros:", data[:5])  # Muestra los primeros 5 registros

    return pd.DataFrame(data)

# Agrega una función para obtener la colección
def get_collection():
    return collection


df = obtener_datos()
print("Estructura de datos:", df.columns)  # Ver las columnas del DataFrame
print("Primeras filas:", df.head())  # Mostrar las primeras filas del DataFrame

""" 
def conectarMongo():       
   try:
        client = MongoClient('mongodb://localhost:27017/')
        db = client['dbTiendaBicicleta']
        return db
   except Exception as e:
        print(f"Error de conexión a la base de datos: {e}")
        return None

def obtenerColeccion():
    db = conectarMongo()
    if db is not None:  # Comparación explícita con None
        return db['VentasBicicleta']
    else:
        print("Error: no se pudo conectar a la base de datos.")
        return None


collection = db['VentasBicicleta'].count_documents({}) #verificar el numero de registros
print(client.list_database_names()) # ver el listado de las bases
print(db.list_collection_names()) #ver la(s) coleccion(es) que esta en la base
print(collection) #ver el registro
"""

#mongoimport --db dbReporteBicicleta --collection VentasBicicleta --type csv --file D:\ReporteBicicleta.csv --headerline 
