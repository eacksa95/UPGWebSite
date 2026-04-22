from django.db import models


class MensajeContacto(models.Model):
    TIPO_CHOICES = [
        ('consulta',      'Consulta general'),
        ('informacion',   'Solicitud de información'),
        ('otro',          'Otro'),
    ]

    nombre   = models.CharField(max_length=200)
    email    = models.EmailField()
    telefono = models.CharField(max_length=30, blank=True)
    asunto   = models.CharField(max_length=300)
    tipo     = models.CharField(max_length=20, choices=TIPO_CHOICES, default='consulta')
    mensaje  = models.TextField()
    leido    = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Mensaje de contacto'
        verbose_name_plural = 'Mensajes de contacto'

    def __str__(self):
        return f'{self.nombre} — {self.asunto}'


class SolicitudInscripcion(models.Model):
    ESTADO_CHOICES = [
        ('pendiente',  'Pendiente'),
        ('contactado', 'Contactado'),
        ('inscripto',  'Inscripto'),
        ('descartado', 'Descartado'),
    ]

    nombre         = models.CharField(max_length=200)
    email          = models.EmailField()
    telefono       = models.CharField(max_length=30)
    carrera_nombre = models.CharField(max_length=200, blank=True, help_text='Nombre de la carrera de interés')
    mensaje        = models.TextField(blank=True)
    estado         = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    notas_internas = models.TextField(blank=True)
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Solicitud de inscripción'
        verbose_name_plural = 'Solicitudes de inscripción'

    def __str__(self):
        return f'{self.nombre} → {self.carrera_nombre or "Sin carrera"}'
