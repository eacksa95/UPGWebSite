from django.contrib import admin
from .models import Facultad, Carrera, Noticia, ContenidoPagina


@admin.register(Facultad)
class FacultadAdmin(admin.ModelAdmin):
    list_display  = ['nombre', 'orden']
    ordering      = ['orden']


@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    list_display   = ['nombre', 'facultad', 'duracion_anos', 'modalidad', 'activa', 'destacada']
    list_filter    = ['facultad', 'activa', 'destacada', 'modalidad']
    search_fields  = ['nombre', 'descripcion']
    prepopulated_fields = {'slug': ('nombre',)}
    list_editable  = ['activa', 'destacada', 'orden'] if False else ['activa', 'destacada']


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display   = ['titulo', 'categoria', 'publicada', 'destacada', 'fecha_publicacion']
    list_filter    = ['categoria', 'publicada', 'destacada']
    search_fields  = ['titulo', 'resumen', 'contenido']
    prepopulated_fields = {'slug': ('titulo',)}
    list_editable  = ['publicada', 'destacada']
    date_hierarchy = 'fecha_publicacion'


@admin.register(ContenidoPagina)
class ContenidoPaginaAdmin(admin.ModelAdmin):
    list_display  = ['clave', 'titulo', 'updated_at']
    search_fields = ['clave', 'titulo']
