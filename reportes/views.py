from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from queries.queries import get_bienes

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def generar_reporte_bienes(request):
    """Genera un reporte de bienes en formato JSON."""
    try:
        bienes = get_bienes()
        return Response({"reporte": bienes}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
