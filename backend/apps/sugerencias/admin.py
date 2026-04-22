from django.contrib import admin
from .models import Sugerencia, Reclamo


@admin.register(Sugerencia)
class SugerenciaAdmin(admin.ModelAdmin):
    list_display  = ['nombre', 'area', 'respondida', 'created_at']
    list_filter   = ['area', 'respondida']
    search_fields = ['nombre', 'email', 'sugerencia']
    list_editable = ['respondida']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'


@admin.register(Reclamo)
class ReclamoAdmin(admin.ModelAdmin):
    list_display  = ['nombre', 'email', 'tipo', 'estado', 'created_at']
    list_filter   = ['tipo', 'estado']
    search_fields = ['nombre', 'email', 'descripcion']
    list_editable = ['estado']
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'created_at'
