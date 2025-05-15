from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import BienSerializer
from queries.queries import (
    get_bienes, get_bien_by_id, create_bien, update_ambiente_bien, delete_image_from_db
)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def list_bienes(request):
    """Obtiene todos los bienes."""
    try:
        bienes = get_bienes()
        
        print(bienes)
        
        return Response(bienes, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def retrieve_bien(request, inventario):
    """Obtiene un bien por su inventario."""
    try:
        bien = get_bien_by_id(inventario)
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
def delete_bien_image(request, image_id):
    """Elimina una imagen asociada a un bien."""
    try:
        delete_image_from_db(image_id)
        return Response({"message": "Imagen eliminada exitosamente."}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


