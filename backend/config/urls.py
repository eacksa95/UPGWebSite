from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/contenido/',   include('apps.contenido.urls')),
    path('api/contacto/',    include('apps.contacto.urls')),
    path('api/sugerencias/', include('apps.sugerencias.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Personalización del admin
admin.site.site_header = 'UPG — Administración'
admin.site.site_title  = 'Panel UPG'
admin.site.index_title = 'Universidad Privada del Guairá'
