from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Sugerencia, Reclamo
from .serializers import SugerenciaSerializer, ReclamoSerializer


@api_view(['POST'])
def crear_sugerencia(request):
    serializer = SugerenciaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'detail': 'Sugerencia enviada. ¡Gracias por contribuir a mejorar la universidad!'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def crear_reclamo(request):
    serializer = ReclamoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'detail': 'Reclamo registrado. Lo revisaremos y daremos respuesta a la brevedad.'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
