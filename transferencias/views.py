from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from queries.queries import (
    registrar_transferencia, get_ambiente_actual_bien
)

# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_transferencia(request):
    """Registra una transferencia de un bien."""
    inventario = request.data.get('inventario')
    ambiente_destino = request.data.get('ambiente_destino')
    fecha_transferencia = request.data.get('fecha_transferencia')

    if not inventario or not ambiente_destino or not fecha_transferencia:
        return Response({"error": "Todos los campos son obligatorios."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        ambiente_origen = get_ambiente_actual_bien(inventario)
        if not ambiente_origen:
            return Response({"error": "El bien no tiene un ambiente actual."}, status=status.HTTP_404_NOT_FOUND)

        registrar_transferencia(inventario, ambiente_origen, ambiente_destino, fecha_transferencia)
        return Response({"message": "Transferencia registrada exitosamente."}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
