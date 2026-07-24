"""
Configuración general de la aplicación.

Este módulo centraliza las rutas de los recursos utilizados por el
sistema, como la base de datos, el esquema SQL, los íconos y las
imágenes empleadas en la interfaz gráfica.
"""

from pathlib import Path

# Directorio raíz del proyecto.
BASE_DIR = Path(__file__).resolve().parent

# Ruta de la base de datos SQLite.
DB_PATH = BASE_DIR / "database" / "data" / "punto_venta.db"

# Ruta del archivo que contiene el esquema de la base de datos.
SCHEMA_PATH = BASE_DIR / "database" / "schema.sql"

# Recursos gráficos de la aplicación.
ICON_PATH = BASE_DIR / "assets" / "icons" / "pos-icon.ico"
IMAGE_POST = BASE_DIR / "assets" / "images" / "pos-image.png"

# Imágenes utilizadas en el panel principal.
ADMIN_IMG = BASE_DIR / "assets" / "images" / "admin.png"
VENTAS_IMG = BASE_DIR / "assets" / "images" / "ventas.png"
ALMACEN_IMG = BASE_DIR / "assets" / "images" / "almacen.png"