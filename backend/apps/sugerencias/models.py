from django.db import models


class Sugerencia(models.Model):
    AREA_CHOICES = [
        ('academico',       'Académico'),
        ('administrativo',  'Administrativo'),
        ('infraestructura', 'Infraestructura'),
        ('tecnologia',      'Tecnología'),
        ('otro',            'Otro'),
    ]

    nombre    = models.CharField(max_length=200, blank=True, help_text='Opcional — puede ser anónimo')
    email     = models.EmailField(blank=True)
    area      = models.CharField(max_length=20, choices=AREA_CHOICES, default='otro')
    sugerencia = models.TextField()
    respondida = models.BooleanField(default=False)
    respuesta  = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Sugerencia'
        verbose_name_plural = 'Sugerencias'

    def __str__(self):
        anon = self.nombre or 'Anónimo'
        return f'{anon} — {self.get_area_display()}'


class Reclamo(models.Model):
    ESTADO_CHOICES = [
        ('abierto',     'Abierto'),
        ('en_proceso',  'En proceso'),
        ('resuelto',    'Resuelto'),
        ('cerrado',     'Cerrado'),
    ]

    TIPO_CHOICES = [
        ('academico',      'Académico'),
        ('administrativo', 'Administrativo'),
        ('docente',        'Docente'),
        ('infraestructura','Infraestructura'),
        ('otro',           'Otro'),
    ]

    nombre    = models.CharField(max_length=200)
    email     = models.EmailField()
    telefono  = models.CharField(max_length=30, blank=True)
    tipo      = models.CharField(max_length=20, choices=TIPO_CHOICES, default='otro')
    descripcion = models.TextField()
    estado    = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='abierto')
    resolucion = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Reclamo'
        verbose_name_plural = 'Reclamos'

    def __str__(self):
        return f'{self.nombre} — {self.get_tipo_display()} [{self.get_estado_display()}]'
