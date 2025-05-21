from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from queries.queries import (
    get_bienes, create_bien, get_bien_by_id,
    get_ambientes, get_ambient_by_id_or_name,
    get_subgrupo, get_secciones_by_subgrupo_id,
    registrar_transferencia, update_ambiente_bien,
    get_imagenes_by_inventario, save_image_to_db
)
import json

# ==============================================
# Funciones para bienes
# ==============================================

def consultar_bienes(request):
    try:
        bienes = get_bienes()
        return JsonResponse(bienes, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def crear_bien(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            create_bien(**data)
            return JsonResponse({'message': 'Bien creado exitosamente'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

def consultar_bien_por_id(request, bien_id):
    try:
        bien = get_bien_by_id(bien_id)
        if bien:
            return JsonResponse(bien, safe=False)
        return JsonResponse({'error': 'Bien no encontrado'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# ==============================================
# Funciones para ambientes
# ==============================================

def consultar_ambientes(request):
    try:
        ambientes = get_ambientes()
        return JsonResponse(ambientes, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def consultar_ambiente_por_id_o_nombre(request, identificador):
    try:
        ambiente = get_ambient_by_id_or_name(identificador)
        if ambiente:
            return JsonResponse(ambiente, safe=False)
        return JsonResponse({'error': 'Ambiente no encontrado'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# ==============================================
# Funciones para grupos
# ==============================================

def consultar_grupos(request):
    try:
        grupos = get_subgrupo()
        return JsonResponse(list(grupos), safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def consultar_secciones_por_grupo(request, grupo_id):
    try:
        secciones = get_secciones_by_subgrupo_id(grupo_id)
        return JsonResponse(list(secciones), safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# ==============================================
# Funciones para transferencias
# ==============================================

@csrf_exempt
def registrar_transferencia_bien(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            registrar_transferencia(**data)
            return JsonResponse({'message': 'Transferencia registrada exitosamente'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def actualizar_ambiente_bien(request, inventario):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            nuevo_ambiente = data.get('nuevo_ambiente')
            update_ambiente_bien(inventario, nuevo_ambiente)
            return JsonResponse({'message': 'Ambiente actualizado exitosamente'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

# ==============================================
# Funciones para imágenes
# ==============================================

def consultar_imagenes_por_inventario(request, inventario):
    try:
        imagenes = get_imagenes_by_inventario(inventario)
        return JsonResponse(list(imagenes), safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def guardar_imagen(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            inventario = data.get('inventario')
            image_path = data.get('image_path')
            save_image_to_db(inventario, image_path)
            return JsonResponse({'message': 'Imagen guardada exitosamente'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
