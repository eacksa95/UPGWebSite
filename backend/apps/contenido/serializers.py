from rest_framework import serializers
from .models import Facultad, Carrera, Noticia, ContenidoPagina


class FacultadSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Facultad
        fields = ['id', 'nombre', 'descripcion', 'color']


class CarreraSerializer(serializers.ModelSerializer):
    facultad_nombre = serializers.CharField(source='facultad.nombre', read_only=True)

    class Meta:
        model  = Carrera
        fields = [
            'id', 'nombre', 'slug', 'facultad', 'facultad_nombre',
            'descripcion_corta', 'descripcion', 'duracion_anos',
            'modalidad', 'titulo_otorgado', 'perfil_egresado',
            'emoji', 'color_acento', 'activa', 'destacada',
        ]


class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Noticia
        fields = [
            'id', 'titulo', 'slug', 'resumen', 'contenido',
            'categoria', 'imagen', 'publicada', 'destacada',
            'fecha_publicacion',
        ]


class ContenidoPaginaSerializer(serializers.ModelSerializer):
    class Meta:
        model  = ContenidoPagina
        fields = ['clave', 'titulo', 'subtitulo', 'cuerpo', 'updated_at']
