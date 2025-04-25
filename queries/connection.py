from sqlalchemy import create_engine, text
import os 
from dotenv import load_dotenv
from enviroment import config

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Define la URL de conexión
usuario = config['DB_USER']
contraseña = config['DB_PASSWORD']
name_db = config['DB_NAME']
host = config['DB_HOST']
port = config['DB_PORT']
url_conexion = f'postgresql://{usuario}:{contraseña}@{host}:{port}/{name_db}'

# Crea el motor de SQLAlchemy
engine = create_engine(url_conexion, pool_pre_ping=True)

# Usa un bloque try-except para manejar la conexión
try:
    with engine.connect() as connection:
        print("conexion exitosa")
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")