from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MensajeContacto, SolicitudInscripcion
from .serializers import MensajeContactoSerializer, SolicitudInscripcionSerializer


@api_view(['POST'])
def crear_mensaje(request):
    serializer = MensajeContactoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'detail': 'Mensaje recibido. Nos contactaremos pronto.'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def crear_solicitud(request):
    serializer = SolicitudInscripcionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'detail': 'Solicitud recibida. Un asesor se comunicará con usted.'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
