from rest_framework import serializers
from .models import Sugerencia, Reclamo


class SugerenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Sugerencia
        fields = ['id', 'nombre', 'email', 'area', 'sugerencia', 'created_at']
        read_only_fields = ['id', 'created_at']


class ReclamoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Reclamo
        fields = ['id', 'nombre', 'email', 'telefono', 'tipo', 'descripcion', 'created_at']
        read_only_fields = ['id', 'created_at']
