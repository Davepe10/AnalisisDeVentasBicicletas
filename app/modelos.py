from .db_conexion import get_collection  # Asegúrate de importar la función para obtener la colección

def obtener_analisis_ventas():
    coleccion = get_collection()  # Obtén la colección directamente
    
    # Total de ventas por ciudad
    ventas_por_ciudad = list(coleccion.aggregate([
        {"$group": {"_id": "$Store_Location", "total_ventas": {"$sum": "$Quantity"}}}
    ]))

    # Edad que más compra bicicletas
    edad_mas_compras = list(coleccion.aggregate([
        {"$group": {"_id": "$Customer_Age", "total_compras": {"$sum": "$Quantity"}}},
        {"$sort": {"total_compras": -1}},
        {"$limit": 1}
    ]))

    # Modelo más vendido
    modelo_mas_vendido = list(coleccion.aggregate([
        {"$group": {"_id": "$Bike_Model", "total_modelos": {"$sum": "$Quantity"}}},
        {"$sort": {"total_modelos": -1}},
        {"$limit": 1}
    ]))

    # Precio que influye en las ventas
    influencia_precio = list(coleccion.aggregate([
        {"$group": {"_id": "$Price", "cantidad_vendida": {"$sum": "$Quantity"}}},
        {"$sort": {"cantidad_vendida": -1}},
        {"$limit": 5}
    ]))

    # Método de pago favorito
    metodo_pago_favorito = list(coleccion.aggregate([
        {"$group": {"_id": "$Payment_Method", "total": {"$sum": 1}}},
        {"$sort": {"total": -1}},
        {"$limit": 1}
    ]))

    # Género y edad promedio de los compradores
    promedio_edad_genero = list(coleccion.aggregate([
        {"$group": {"_id": "$Customer_Gender", "edad_promedio": {"$avg": "$Customer_Age"}}}
    ]))

    # Modelo de bicicleta más vendido por localidad
    modelo_por_localidad = list(coleccion.aggregate([
        {"$group": {"_id": {"Store_Location": "$Store_Location", "Bike_Model": "$Bike_Model"}, "total_ventas": {"$sum": "$Quantity"}}},
        {"$sort": {"_id.Store_Location": 1, "total_ventas": -1}},
        {"$limit": 5}
    ]))

    # Método de pago más usado por ubicación
    metodo_pago_por_localidad = list(coleccion.aggregate([
        {"$group": {"_id": {"Store_Location": "$Store_Location", "Payment_Method": "$Payment_Method"}, "total": {"$sum": 1}}},
        {"$sort": {"_id.Store_Location": 1, "total": -1}},
        {"$limit": 5}
    ]))

    # Método de pago más usado por edad
    metodo_pago_por_edad = list(coleccion.aggregate([
        {"$group": {"_id": {"Customer_Age": "$Customer_Age", "Payment_Method": "$Payment_Method"}, "total": {"$sum": 1}}},
        {"$sort": {"_id.Customer_Age": 1, "total": -1}},
        {"$limit": 5}
    ]))

    return {
        "ventas_por_ciudad": ventas_por_ciudad,
        "edad_mas_compras": edad_mas_compras,
        "modelo_mas_vendido": modelo_mas_vendido,
        "influencia_precio": (influencia_precio),
        "metodo_pago_favorito": (metodo_pago_favorito),
        "promedio_edad_genero": promedio_edad_genero,
        "modelo_por_localidad": (modelo_por_localidad),
        "metodo_pago_por_localidad": (metodo_pago_por_localidad),
        "metodo_pago_por_edad": (metodo_pago_por_edad)
    }

