from django.urls import path
from . import views

urlpatterns = [
    path('mensaje/',   views.crear_mensaje),
    path('solicitud/', views.crear_solicitud),
]
