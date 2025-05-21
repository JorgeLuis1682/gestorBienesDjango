from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import BienSerializer
from queries.queries import (
    get_bienes, get_bien_by_id, create_bien, update_ambiente_bien, delete_image_from_db, get_imagenes_by_inventario, save_image_to_db
)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def save_image_to_db_rest(request):
    """Guarda una imagen en la base de datos."""
    try:
        inventario = request.data.get('inventario')
        image_path = request.data.get('image_path')
        if not inventario or not image_path:
            return Response({"error": "El inventario y la ruta de la imagen son obligatorios."}, status=status.HTTP_400_BAD_REQUEST)
        save_image_to_db(inventario, image_path)
        return Response({"message": "Imagen subida exitosamente."}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def list_bienes(request):
    """Obtiene todos los bienes."""
    try:
        bienes = get_bienes()        
        return Response(bienes, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def retrieve_bien(request, inventario):
    """Obtiene un bien por su inventario."""
    try:
        bien = get_bien_by_id(inventario)
        
        print(bien)
        if not bien:
            return Response({"error": "Bien no encontrado."}, status=status.HTTP_404_NOT_FOUND)
        return Response(dict(bien), status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def create_bien_view(request):
    """Crea un nuevo bien."""
    try:
        create_bien(**request.data)
        return Response({"message": "Bien creado exitosamente."}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
# @permission_classes([IsAuthenticated])
def update_bien_ambiente(request, inventario):
    """Actualiza el ambiente de un bien."""
    nuevo_ambiente = request.data.get('nuevo_ambiente')
    if not nuevo_ambiente:
        return Response({"error": "El nuevo ambiente es obligatorio."}, status=status.HTTP_400_BAD_REQUEST)
    try:
        update_ambiente_bien(inventario, nuevo_ambiente)
        return Response({"message": "Ambiente actualizado exitosamente."}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def delete_bien_image(request, inventario):
    """Elimina una imagen asociada a un bien."""
    try:
        image_id = request.data.get('image_id')
        if not image_id:
            return Response({"error": "El ID de la imagen es obligatorio."}, status=status.HTTP_400_BAD_REQUEST)
        delete_image_from_db(image_id)
        return Response({"message": "Imagen eliminada exitosamente."}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def list_bien_images(request, inventario):
    """Lista las imágenes asociadas a un bien."""
    try:
        imagenes = get_imagenes_by_inventario(inventario)
        imagenes_list = [{'id': img.id, 'url': img.url} for img in imagenes]
        return Response(imagenes_list, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def upload_bien_image(request, inventario):
    """Sube una imagen asociada a un bien."""
    try:
        image_path = request.data.get('image_path')
        if not image_path:
            return Response({"error": "La ruta de la imagen es obligatoria."}, status=status.HTTP_400_BAD_REQUEST)
        save_image_to_db(inventario, image_path)
        return Response({"message": "Imagen subida exitosamente."}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
# @permission_classes([IsAuthenticated])
def update_bien_image(request, inventario):
    """Actualiza el ambiente de un bien relacionado con una imagen."""
    try:
        nuevo_ambiente = request.data.get('nuevo_ambiente')
        if not nuevo_ambiente:
            return Response({"error": "El nuevo ambiente es obligatorio."}, status=status.HTTP_400_BAD_REQUEST)
        update_ambiente_bien(inventario, nuevo_ambiente)
        return Response({"message": "Ambiente actualizado exitosamente."}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


