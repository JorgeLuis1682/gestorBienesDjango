import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener el entorno actual
environment = os.getenv('ENV', 'local')

config = {
    'DB_HOST': '',
    'DB_PORT': '',
    'DB_USER': '',
    'DB_PASSWORD': '',
    'DB_NAME': 'inventario',
    'SUPABASE_URL': '',
    'SUPABASE_KEY': '',
    'USER_DEV_EMAIL': '',
    'USER_DEV_PASSWORD': '',
}

if environment == 'local':
    config['DB_HOST'] = os.getenv('DB_HOST')
    config['DB_PORT'] = os.getenv('DB_PORT')
    config['DB_USER'] = os.getenv('DB_USER')
    config['DB_PASSWORD'] = os.getenv('DB_PASSWORD')
    config['DB_NAME'] = os.getenv('DB_NAME')
elif environment == 'qa':
    config['DB_HOST'] = os.getenv('DB_HOST')
    config['DB_PORT'] = os.getenv('DB_PORT')
    config['DB_USER'] = os.getenv('DB_USER')
    config['DB_PASSWORD'] = os.getenv('DB_PASSWORD')
    config['DB_NAME'] = os.getenv('DB_NAME')
    config['SUPABASE_URL'] = os.getenv('SUPABASE_URL')
    config['SUPABASE_KEY'] = os.getenv('SUPABASE_KEY')
    config['USER_DEV_EMAIL'] = os.getenv('USER_DEV_EMAIL')
    config['USER_DEV_PASSWORD'] = os.getenv('USER_DEV_PASSWORD')
elif environment == 'prod':
    config['DB_HOST'] = os.getenv('DB_HOST_PROD')
    config['DB_PORT'] = os.getenv('DB_PORT_PROD')
    config['DB_USER'] = os.getenv('DB_USER_PROD')
    config['DB_PASSWORD'] = os.getenv('DB_PASSWORD_PROD')
else:
    raise ValueError(f"Entorno desconocido: {environment}")

# Imprimir la configuración para verificar
print(f"Configuración para el entorno {environment}:")
print(config)