# import sqlalchemy as db
# from sqlalchemy import text
# from connection import engine
# import os
# import io
# import shutil
# -- coding: utf-8 --

"""----------------------------------------------------------------------------
----------------------------------------------------------------------------------
-----------------------------------------------------------------------------"""

import sqlalchemy as db
from sqlalchemy import text
from .connection import engine
import os
import io
import shutil

# ==============================================
# Funciones para el manejo de imágenes
# ==============================================

# ==============================================
# Funciones para el manejo de imágenes
# ==============================================

def get_imagenes_by_inventario(inventario):
    """Obtiene todas las imágenes asociadas a un número de inventario"""
    with engine.connect() as connection:
        result = connection.execute(
            text('SELECT id, url FROM public.imagenes WHERE inventario = :inventario'),
            {'inventario': inventario}
        )
        return result

def save_image_to_db(inventario, image_path):
    """Guarda la ruta de la imagen en la base de datos"""
    with engine.connect() as connection:
        connection.execute(
            text('INSERT INTO public.imagenes (inventario, url) VALUES (:inventario, :url)'),
            {
                'inventario': inventario,
                'url': image_path
            }
        )
        connection.commit()
        return True

def delete_image_from_db(image_id):
    """Elimina una imagen de la base de datos por su ID"""
    with engine.connect() as connection:
        connection.execute(
            text('DELETE FROM public.imagenes WHERE id = :image_id'),
            {'image_id': image_id}
        )
        connection.commit()
        return True

def guardar_imagen_en_sistema(inventario, filepath):
    """Guarda físicamente la imagen en el sistema de archivos"""
    try:
        # Crear directorio si no existe
        directorio_imagenes = os.path.join("imagenes_bienes", inventario)
        os.makedirs(directorio_imagenes, exist_ok=True)
        
        # Copiar la imagen al directorio
        nombre_archivo = os.path.basename(filepath)
        destino = os.path.join(directorio_imagenes, nombre_archivo)
        shutil.copy(filepath, destino)
        
        # Retornar ruta relativa para guardar en BD
        return os.path.join("imagenes_bienes", inventario, nombre_archivo)
    except Exception as e:
        raise Exception(f"Error al guardar imagen en sistema: {str(e)}")


# Funcion para crear un bien

def create_bien(inventario, descripcion, idsubgrupo, idseccion, valor, idunidaddetrabajo, idambiente, factura, fechafactura, fechaincorporacion, desincorporado, robado, chatarra, fechadesincorporacion, vidautil, valorderecuparacion, valordedepreciacion, faltante, esperafactura, danado, otros, otrosmemo, fuerademural, observaciones, codigop, vehiculo, maquinaria, marcadorgrupal, mantenimiento, esrecolector, moto, inspeccion, fechaultimainspeccion, iddependencias, inservible, codigopresupuestario, sc, valorsoberano, trial460):
    try:
        with engine.connect() as connection:
            result = connection.execute(text(f'''
            INSERT INTO bienes
            (inventario, descripción, idsubgrupo, idsección, valor, idunidaddetrabajo, idambiente, factura, fechafactura, fechaincorporación, desincorporado, robado, chatarra, fechadesincorporación, vidaútil, valorderecuparación, valordedepreciación, faltante, esperafactura, dañado, otros, otrosmemo, fuerademural, observaciones, códigop, vehículo, maquinaria, "marcador grupal", mantenimiento, esrecolector, moto, inspección, "fecha última inspección", iddependencias, inservible, codigopresupuestario, sc, valorsoberano, trial460)
            VALUES('{inventario}', '{descripcion}', {idsubgrupo}, {idseccion}, {valor}, {idunidaddetrabajo}, {idambiente}, '{factura}', '{fechafactura}', '{fechaincorporacion}', {desincorporado}, {robado}, {chatarra}, '{fechadesincorporacion}', {vidautil}, {valorderecuparacion}, {valordedepreciacion}, {faltante}, {esperafactura}, {danado}, {otros}, '{otrosmemo}', {fuerademural}, '{observaciones}', '{codigop}', {vehiculo}, {maquinaria}, {marcadorgrupal}, {mantenimiento}, {esrecolector}, {moto}, {inspeccion}, '{fechaultimainspeccion}', {iddependencias}, {inservible}, '{codigopresupuestario}', {sc}, {valorsoberano}, '{trial460}');
            '''))
            
            connection.commit()
            
            return result
    except Exception as e:
        print(f"Error al crear bien: {e}")

'''

Prueba para la funcion de crear un bien en la base de datos


 create_bien('2', 'prueba', 1, 1, 100, 1, 1, 'factura', '2021-01-01', '2021-01-01', False, False, False, '2021-01-01', 10, 10, 10, False, False, False, False, 'memo', False, 'm3mo', 'codigop', False, False, False, False, False, False, False, '2021-01-01', 1, False, 'memo', True, 1.0, 'T')
'''


# Función para obtener todos los bienes
# querie para "actualizar bien" en este caso usamos el ejemplo del "1121" con sus valores ya creados,
# para actualizar un bien se debe usar el "inventario" del bien que se desea actualizar
'''
UPDATE public.bienes
SET descripción='Mouse marca: HP sin serial', idsubgrupo=13, idsección=86, valor=0.0, idunidaddetrabajo=1, idambiente=137, factura=NULL, fechafactura=NULL, fechaincorporación='2024-12-13 00:00:00.000', desincorporado=false, robado=false, chatarra=false, fechadesincorporación=NULL, vidaútil=NULL, valorderecuparación=NULL, valordedepreciación=NULL, faltante=false, esperafactura=true, dañado=false, otros=false, otrosmemo=NULL, fuerademural=false, observaciones='Placa en resguardo', códigop=NULL, vehículo=false, maquinaria=false, "marcador grupal"=false, mantenimiento=false, esrecolector=false, moto=false, inspección=true, "fecha última inspección"='2024-12-13 00:00:00.000', iddependencias=NULL, inservible=false, codigopresupuestario=NULL, sc=false, valorsoberano=NULL, trial460='T'
WHERE inventario='6495';
'''

# Funcion para crear un bien

def create_bien(inventario, descripcion, idsubgrupo, idseccion, valor, idunidaddetrabajo, idambiente, factura, fechafactura, fechaincorporacion, desincorporado, robado, chatarra, fechadesincorporacion, vidautil, valorderecuparacion, valordedepreciacion, faltante, esperafactura, danado, otros, otrosmemo, fuerademural, observaciones, codigop, vehiculo, maquinaria, marcadorgrupal, mantenimiento, esrecolector, moto, inspeccion, fechaultimainspeccion, iddependencias, inservible, codigopresupuestario, sc, valorsoberano, trial460):
    try:
        with engine.connect() as connection:
            result = connection.execute(text(f'''
            INSERT INTO bienes
            (inventario, descripción, idsubgrupo, idsección, valor, idunidaddetrabajo, idambiente, factura, fechafactura, fechaincorporación, desincorporado, robado, chatarra, fechadesincorporación, vidaútil, valorderecuparación, valordedepreciación, faltante, esperafactura, dañado, otros, otrosmemo, fuerademural, observaciones, códigop, vehículo, maquinaria, "marcador grupal", mantenimiento, esrecolector, moto, inspección, "fecha última inspección", iddependencias, inservible, codigopresupuestario, sc, valorsoberano, trial460)
            VALUES('{inventario}', '{descripcion}', {idsubgrupo}, {idseccion}, {valor}, {idunidaddetrabajo}, {idambiente}, '{factura}', '{fechafactura}', '{fechaincorporacion}', {desincorporado}, {robado}, {chatarra}, '{fechadesincorporacion}', {vidautil}, {valorderecuparacion}, {valordedepreciacion}, {faltante}, {esperafactura}, {danado}, {otros}, '{otrosmemo}', {fuerademural}, '{observaciones}', '{codigop}', {vehiculo}, {maquinaria}, {marcadorgrupal}, {mantenimiento}, {esrecolector}, {moto}, {inspeccion}, '{fechaultimainspeccion}', {iddependencias}, {inservible}, '{codigopresupuestario}', {sc}, {valorsoberano}, '{trial460}');
            '''))
            
            connection.commit()
            
            return result
    except Exception as e:
        print(f"Error al crear bien: {e}")

'''

Prueba para la funcion de crear un bien en la base de datos
 create_bien('2', 'prueba', 1, 1, 100, 1, 1, 'factura', '2021-01-01', '2021-01-01', False, False, False, '2021-01-01', 10, 10, 10, False, False, False, False, 'memo', False, 'm3mo', 'codigop', False, False, False, False, False, False, False, '2021-01-01', 1, False, 'memo', True, 1.0, 'T')
'''

keys_to_bien = [
    'inventario', 'descripción', 'idsubgrupo', 'idsección', 'valor',
    'idunidaddetrabajo', 'idambiente', 'factura', 'fechafactura',
    'fechaincorporación', 'desincorporado', 'robado', 'chatarra',
    'fechadesincorporacion', 'vidaútil', 'valorderecuparación',
    'valordedepreciación', 'faltante', 'esperafactura', 'dañado',
    'otros', 'otrosmemo', 'fuerademural', 'observaciones', 'códigop',
    'vehículo', 'maquinaria', 'marcador grupal', 'mantenimiento',
    'esrecolector', 'moto', 'inspección', 'fecha última inspección',
    'iddependencias', 'inservible', 'codigopresupuestario', 'sc',
    'valorsoberano', 'trial460'
]


# Función para obtener todos los bienes
def get_bienes():
    try: 
        with engine.connect() as connection:
            lista_bienes = []
            result = connection.execute(text('''SELECT * FROM bienes;''')).all()
            lista_bienes = [dict(zip(keys_to_bien, row)) for row in result]
            print(lista_bienes)
            return lista_bienes 
    except Exception as e:
        print(f"Error: {e}")
        return []
        
        
def get_subgrupo():
    try:
        with engine.connect() as connection:
            result = connection.execute(text('''SELECT * FROM public.subgrupo;'''))
            # for row in result:
              #  print(row)
            return result
    except Exception as e:
        print(f'error as {e}')
        
def get_ambientes():
    try:
        with engine.connect() as connection:
            result = connection.execute(text('''SELECT * FROM ambientes;'''))
            return [dict(row) for row in result]  # Convertir a lista de diccionarios
    except Exception as e:
        print(f"Error: {e}")
        
def get_ambient_by_id_or_name(identificador):
    """Obtiene un ambiente por su ID o nombre."""
    try:
        with engine.connect() as connection:
            if identificador.isdigit():
                # Buscar por ID
                result = connection.execute(
                    text('SELECT * FROM ambientes WHERE idambiente = :idambiente'),
                    {'idambiente': int(identificador)}
                )
            else:
                # Buscar por nombre
                result = connection.execute(
                    text('SELECT * FROM ambientes WHERE nombreambiente = :nombreambiente'),
                    {'nombreambiente': identificador}
                )
            return result.fetchone()  # Retorna el primer resultado o None si no existe
    except Exception as e:
        print(f"Error al obtener el ambiente por ID o nombre: {e}")
        return None
        
def get_bien_by_id(id):
    try:
        with engine.connect() as connection:
            result = connection.execute(text(f'''SELECT * FROM bienes WHERE inventario = '{id}';''')).fetchone()
            # for row in result: 
            #     print(row)
            return dict(zip(keys_to_bien, result))
    except Exception as e:
        print(f"Error: {e}")
        
def get_one_value_on_bien(id, value):
    try:
        with engine.connect() as connection:
            result = connection.execute(text(f'''SELECT bienes.{value} FROM bienes WHERE inventario = '{id}';'''))
            #for row in result:
             # print(row)
            return result
    except Exception as e:
        print(f"Error: {e}")
        
def get_bien_by_subgrupo_by_id(subgrupo_id):
    try:
        with engine.connect() as connection:
            result = connection.execute(text(f'''SELECT *  FROM subgrupo WHERE subgrupo.idsubgrupo = {subgrupo_id};'''))
            #for row in result:
             # print(row)
            return result
    except Exception as e:
        print(f"Error: {e}")
        
        
def get_bien_by_unidad_by_id(unidad_id):
    try:
        with engine.connect() as connection:
            result = connection.execute(text(f'''SELECT * FROM "unidad de trabajo" where "unidad de trabajo".idunidaddetrabajo   = {unidad_id};'''))
            #for row in result:
             # print(row)
            return result
    except Exception as e:
        print(f"Error: {e}")
        
        
    
def get_ambient_by_id(ambient_id):
    """Obtiene un ambiente por su ID."""
    try:
        with engine.connect() as connection:
            result = connection.execute(
                text('SELECT * FROM ambientes WHERE idambiente = :idambiente'),
                {'idambiente': ambient_id}
            )
            return result.fetchone()  # Retorna el primer resultado o None si no existe
    except Exception as e:
        print(f"Error al obtener el ambiente por ID: {e}")
        return None
           
def get_bien_by_ambient_by_id(identificador):
    """Obtiene bienes por ID o nombre de ambiente."""
    try:
        with engine.connect() as connection:
            query = ''
            params = {}

            if identificador.isdigit():
                # Buscar por ID de ambiente
                query = 'SELECT * FROM bienes WHERE idambiente = :idambiente'
                params = {'idambiente': int(identificador)}
            else:
                # Buscar por nombre de ambiente
                query = '''
                    SELECT b.* 
                    FROM bienes b
                    JOIN ambientes a ON b.idambiente = a.idambiente
                    WHERE a.nombreambiente = :nombreambiente
                '''
                params = {'nombreambiente': identificador}

            result = connection.execute(text(query), params)
            return result.fetchall()  # Retornar todos los resultados como lista
    except Exception as e:
        print(f"Error al obtener bienes por ambiente: {e}")
        return []

def get_unidad_de_trabajo():
    try:
        with engine.connect() as connection:
            result = connection.execute(text('''SELECT * FROM public."unidad de trabajo";'''))
            return [dict(row) for row in result]  # Convertir a lista de diccionarios
    except Exception as e:
        print(f"Error: {e}")

def get_seccion_by_id(seccion_id):
    try:
        with engine.connect() as connection:
            result = connection.execute(text(f'''SELECT * FROM bienes where bienes.idsección  = {seccion_id};'''))
            # for row in result:
            #     print(row)
            return result
    except Exception as e:
        print(f"Error: {e}")
        
def get_secciones():
    try:
        with engine.connect() as connection:
            result = connection.execute(text('''SELECT * FROM public.sección;'''))
            # for row in result:
              #  print(row)
            return result
    except Exception as e:
        print(f"Error: {e}")
        

# Nuevas funciones para transferencias
def get_ambiente_actual_bien(inventario):
    try:
        with engine.connect() as connection:
            result = connection.execute(text(f'''SELECT idambiente FROM bienes WHERE inventario = '{inventario}';'''))
            return result.fetchone()[0]  # Devuelve el id del ambiente actual
    except Exception as e:
        print(f"Error: {e}")
        return None

def update_ambiente_bien(inventario, nuevo_ambiente):
    """Actualiza el ambiente de un bien"""
    with engine.connect() as connection:
        connection.execute(
            text('UPDATE bienes SET idambiente = :nuevo_ambiente WHERE inventario = :inventario'),
            {
                'nuevo_ambiente': nuevo_ambiente,
                'inventario': inventario
            }
        )
        connection.commit()

def registrar_transferencia(inventario, ambiente_origen, ambiente_destino, fecha_transferencia):
    """Registra una transferencia de bien entre ambientes"""
    with engine.connect() as connection:
        connection.execute(
            text('''
                INSERT INTO transferencias 
                (inventario, idambienteorigen, idambientedestino, fechatransferencia)
                VALUES (:inventario, :ambiente_origen, :ambiente_destino, :fecha_transferencia)
            '''),
            {
                'inventario': inventario,
                'ambiente_origen': ambiente_origen,
                'ambiente_destino': ambiente_destino,
                'fecha_transferencia': fecha_transferencia
            }
        )
        connection.commit()
        
def get_bien_by_subgrupo_by_id(subgrupo_id):
    """Obtiene bienes por ID de subgrupo"""
    with engine.connect() as connection:
        result = connection.execute(
            text('SELECT * FROM subgrupo WHERE idsubgrupo = :subgrupo_id'),
            {'subgrupo_id': subgrupo_id}
        )
        return result

def get_secciones_by_subgrupo_id(subgrupo_id):
    """Obtiene secciones filtradas por ID de subgrupo"""
    with engine.connect() as connection:
        result = connection.execute(
            text('SELECT * FROM "sección" WHERE "idsubgrupo" = :subgrupo_id ORDER BY "nombresección"'),
            {'subgrupo_id': subgrupo_id}
        )
        return result

def get_subgrupo_id_by_name(subgrupo_name):
    """Obtiene el ID de un subgrupo por su nombre"""
    with engine.connect() as connection:
        result = connection.execute(
            text('SELECT "idsubgrupo" FROM subgrupo WHERE "nombresubgrupo" = :subgrupo_name'),
            {'subgrupo_name': subgrupo_name}
        )
        return result.scalar()

def get_seccion_id_by_name(seccion_name):
    """Obtiene el ID de una sección por su nombre"""
    with engine.connect() as connection:
        result = connection.execute(
            text('SELECT "idsección" FROM "sección" WHERE "nombresección" = :seccion_name'),
            {'seccion_name': seccion_name}
        )
        return result.scalar()
    
# def get_ambiente_id_by_name(ambiente_name):
#     """Obtiene el ID de un ambiente por su nombre"""
#     with engine.connect() as connection:
#         result = connection.execute(
#             text('SELECT "idambiente" FROM ambientes WHERE "nombreambiente" = :ambiente_name'),
#             {'ambiente_name': ambiente_name}
#         )
#         return result.scalar()
    
def get_unidad_id_by_name(unidad_name):
    """Obtiene el ID de una unidad de trabajo por su nombre"""
    with engine.connect() as connection:
        result = connection.execute(
            text('SELECT "idunidaddetrabajo" FROM "unidad de trabajo" WHERE "nombreunidad" = :unidad_name'),
            {'unidad_name': unidad_name}
        )
        return result.scalar()

def get_ambientes_by_unidad_id(unidad_id):
    """Obtiene ambientes filtrados por ID de unidad de trabajo"""
    with engine.connect() as connection:
        result = connection.execute(
            text('SELECT * FROM ambientes WHERE "idunidaddetrabajo" = :unidad_id ORDER BY "nombreambiente"'),
            {'unidad_id': unidad_id}
        )
        return result

def get_ambientes_by_unidad_name(unidad_name):
    """Obtiene todos los ambientes asociados al nombre de una unidad de trabajo."""
    try:
        with engine.connect() as connection:
            # Obtener el ID de la unidad de trabajo por su nombre
            unidad_id = connection.execute(
                text('SELECT idunidaddetrabajo FROM "unidad de trabajo" WHERE unidaddetrabajo = :unidad_name'),
                {'unidad_name': unidad_name}
            ).scalar()

            if not unidad_id:
                raise ValueError(f"No se encontró una unidad de trabajo con el nombre '{unidad_name}'.")

            # Consultar los ambientes asociados al ID de la unidad de trabajo
            result = connection.execute(
                text('''
                    SELECT idambiente, nombreambiente, idunidaddetrabajo, "observaciones bm-3", trial453
                    FROM public.ambientes
                    WHERE idunidaddetrabajo = :unidad_id
                '''),
                {'unidad_id': unidad_id}
            )
            return result.fetchall()  # Retornar todos los resultados como lista
    except Exception as e:
        print(f"Error al obtener los ambientes por unidad de trabajo: {e}")
        return []

def get_dependencias():
    """Obtiene todas las dependencias"""
    with engine.connect() as connection:
        result = connection.execute(text('''SELECT * FROM public.dependencias;'''))
        return result 
    
def get_dependencia_by_id(dependencia_id):
    """Obtiene una dependencia por su ID"""
    with engine.connect() as connection:
        result = connection.execute(
            text('SELECT * FROM dependencias WHERE iddependencias = :dependencia_id'),
            {'dependencia_id': dependencia_id}
        )
        return result.fetchone()
    
    
def get_dependencia_id_by_name(dependencia_name):
    """Obtiene el ID de una dependencia por su nombre"""
    with engine.connect() as connection:
        result = connection.execute(
            text('SELECT iddependencias FROM dependencias WHERE nombrededependencia = :dependencia_name'),
            {'dependencia_name': dependencia_name}
        )
        return result.scalar()

