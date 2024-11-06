from flask import Flask
from app.rutas import app as rutas_bp  # Asegúrate de que esto apunte correctamente

def create_app():
    app = Flask(__name__)

    # Registrar el blueprint
    app.register_blueprint(rutas_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)  # Modo de depuración para ver errores
