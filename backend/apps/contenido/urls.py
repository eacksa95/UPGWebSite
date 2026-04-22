from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('facultades', views.FacultadViewSet)
router.register('carreras',   views.CarreraViewSet)
router.register('noticias',   views.NoticiaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('pagina/<str:clave>/', views.contenido_por_clave),
]
