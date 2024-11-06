from .db_conexion import get_database
from .modelos import VentasBicicleta

def crear_dashboard():
    """Crea los datos necesarios para el dashboard."""
    db = get_database()
    if db is None:
        return None
    
    # Obtén los datos de la colección
    try:
        ventas = db['datosBicicleta'].find()
        datos = [VentasBicicleta.from_dict(venta) for venta in ventas]
        return datos
    except Exception as e:
        print(f"Error al obtener datos: {e}")
        return None
