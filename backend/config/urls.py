from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    # Frontend — servido como templates estáticos
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('pages/carreras.html', TemplateView.as_view(template_name='pages/carreras.html')),
    path('pages/contacto.html', TemplateView.as_view(template_name='pages/contacto.html')),

    # Backend
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
