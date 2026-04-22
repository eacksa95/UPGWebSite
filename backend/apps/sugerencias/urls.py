from django.urls import path
from . import views

urlpatterns = [
    path('sugerencia/', views.crear_sugerencia),
    path('reclamo/',    views.crear_reclamo),
]
