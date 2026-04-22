from rest_framework import serializers
from .models import MensajeContacto, SolicitudInscripcion


class MensajeContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = MensajeContacto
        fields = ['id', 'nombre', 'email', 'telefono', 'asunto', 'tipo', 'mensaje', 'created_at']
        read_only_fields = ['id', 'created_at']


class SolicitudInscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model  = SolicitudInscripcion
        fields = ['id', 'nombre', 'email', 'telefono', 'carrera_nombre', 'mensaje', 'created_at']
        read_only_fields = ['id', 'created_at']
