from rest_framework import viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Facultad, Carrera, Noticia, ContenidoPagina
from .serializers import FacultadSerializer, CarreraSerializer, NoticiaSerializer, ContenidoPaginaSerializer


class FacultadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset         = Facultad.objects.all()
    serializer_class = FacultadSerializer


class CarreraViewSet(viewsets.ReadOnlyModelViewSet):
    queryset         = Carrera.objects.filter(activa=True).select_related('facultad')
    serializer_class = CarreraSerializer
    filter_backends  = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['facultad', 'modalidad', 'destacada']
    search_fields    = ['nombre', 'descripcion']


class NoticiaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset         = Noticia.objects.filter(publicada=True)
    serializer_class = NoticiaSerializer
    filter_backends  = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['categoria', 'destacada']
    search_fields    = ['titulo', 'resumen']
    lookup_field     = 'slug'


@api_view(['GET'])
def contenido_por_clave(request, clave):
    """Devuelve el contenido editable de una sección de la web."""
    try:
        obj = ContenidoPagina.objects.get(clave=clave)
        return Response(ContenidoPaginaSerializer(obj).data)
    except ContenidoPagina.DoesNotExist:
        return Response({'detail': 'No encontrado'}, status=404)
