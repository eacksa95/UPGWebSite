from django.contrib import admin
from .models import MensajeContacto, SolicitudInscripcion


@admin.register(MensajeContacto)
class MensajeContactoAdmin(admin.ModelAdmin):
    list_display  = ['nombre', 'email', 'tipo', 'asunto', 'leido', 'created_at']
    list_filter   = ['tipo', 'leido']
    search_fields = ['nombre', 'email', 'asunto', 'mensaje']
    list_editable = ['leido']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'


@admin.register(SolicitudInscripcion)
class SolicitudInscripcionAdmin(admin.ModelAdmin):
    list_display  = ['nombre', 'email', 'carrera_nombre', 'estado', 'created_at']
    list_filter   = ['estado']
    search_fields = ['nombre', 'email', 'carrera_nombre']
    list_editable = ['estado']
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'created_at'
