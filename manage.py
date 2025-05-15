#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import enviroment # Importar el archivo de configuración de entorno
import queries.connection # Importar el archivo de conexión a la base de datos
from dotenv import load_dotenv


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestor_bienes.settings')
    try:
        from django.core.management import execute_from_command_line
        load_dotenv()  # Cargar las variables de entorno desde el archivo .env
        # Obtener el entorno actual
        environment = os.getenv('ENV', 'local')
        config = enviroment.config
        # Imprimir la configuración para verificar
        print(f"Configuración para el entorno {environment}:")
        print(config)
        connection = queries.connection.engine
        print("conexion exitosa")
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
