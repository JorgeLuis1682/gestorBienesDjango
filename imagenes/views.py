from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from queries.queries import (
    get_imagenes_by_inventario, save_image_to_db, delete_image_from_db
)

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_imagenes(request, inventario):
    """Obtiene todas las imágenes asociadas a un bien."""
    try:
        imagenes = get_imagenes_by_inventario(inventario)
        return Response([dict(img) for img in imagenes], status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_imagen(request):
    """Guarda una imagen asociada a un bien."""
    inventario = request.data.get('inventario')
    image_path = request.data.get('image_path')

    if not inventario or not image_path:
        return Response({"error": "Inventario e imagen son obligatorios."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        save_image_to_db(inventario, image_path)
        return Response({"message": "Imagen guardada exitosamente."}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_imagen(request, image_id):
    """Elimina una imagen por su ID."""
    try:
        delete_image_from_db(image_id)
        return Response({"message": "Imagen eliminada exitosamente."}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
