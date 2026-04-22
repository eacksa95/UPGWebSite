from django.db import models


class Facultad(models.Model):
    nombre      = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    color       = models.CharField(max_length=7, default='#1B3D6E', help_text='Color hex para la UI')
    orden       = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['orden', 'nombre']
        verbose_name = 'Facultad'
        verbose_name_plural = 'Facultades'

    def __str__(self):
        return self.nombre


class Carrera(models.Model):
    MODALIDAD_CHOICES = [
        ('presencial', 'Presencial'),
        ('semipresencial', 'Semipresencial'),
        ('virtual', 'Virtual'),
    ]

    facultad       = models.ForeignKey(Facultad, on_delete=models.SET_NULL, null=True, related_name='carreras')
    nombre         = models.CharField(max_length=200)
    slug           = models.SlugField(unique=True)
    descripcion    = models.TextField()
    descripcion_corta = models.CharField(max_length=300, blank=True)
    duracion_anos  = models.PositiveSmallIntegerField(default=5)
    modalidad      = models.CharField(max_length=20, choices=MODALIDAD_CHOICES, default='presencial')
    titulo_otorgado = models.CharField(max_length=200, blank=True)
    perfil_egresado = models.TextField(blank=True)
    emoji          = models.CharField(max_length=10, default='🎓')
    color_acento   = models.CharField(max_length=7, default='#1B3D6E')
    activa         = models.BooleanField(default=True)
    destacada      = models.BooleanField(default=False)
    orden          = models.PositiveIntegerField(default=0)
    created_at     = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['orden', 'nombre']
        verbose_name = 'Carrera'
        verbose_name_plural = 'Carreras'

    def __str__(self):
        return self.nombre


class Noticia(models.Model):
    CATEGORIA_CHOICES = [
        ('academico',      'Académico'),
        ('investigacion',  'Investigación'),
        ('cultural',       'Cultural y Deportivo'),
        ('institucional',  'Institucional'),
        ('logros',         'Logros'),
    ]

    titulo      = models.CharField(max_length=300)
    slug        = models.SlugField(unique=True)
    resumen     = models.CharField(max_length=500)
    contenido   = models.TextField()
    categoria   = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default='institucional')
    imagen      = models.ImageField(upload_to='noticias/', blank=True, null=True)
    publicada   = models.BooleanField(default=False)
    destacada   = models.BooleanField(default=False)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-fecha_publicacion']
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'

    def __str__(self):
        return self.titulo


class ContenidoPagina(models.Model):
    """Textos editables de la web (hero, misión, visión, etc.)"""
    clave       = models.CharField(max_length=100, unique=True, help_text='Identificador único. Ej: hero_titulo')
    titulo      = models.CharField(max_length=300, blank=True)
    subtitulo   = models.CharField(max_length=300, blank=True)
    cuerpo      = models.TextField(blank=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Contenido de página'
        verbose_name_plural = 'Contenidos de páginas'

    def __str__(self):
        return self.clave
