# UPGWebSite — Sitio Web Oficial

Sitio web institucional de la **Universidad Privada del Guairá (UPG)**, desarrollado como proyecto de pasantía de la Licenciatura en Ciencias Informáticas de la Universidad Nacional de Asunción Filial Villarrica — Facultad Politécnica.

**Autor:** Ezequiel Alejandro Cristaldo Krechuk  
**Institución cliente:** Universidad Privada del Guairá, Villarrica, Paraguay  
**Año:** 2026

---

## Descripción

Aplicación web completa que incluye:
- Presentación institucional y carreras de grado
- Sistema de noticias y novedades
- Formulario de contacto, sugerencias y reclamos
- Solicitudes de inscripción
- Panel de administración para gestión de contenidos

---

## Stack tecnológico

| Capa | Tecnología |
|---|---|
| Frontend | HTML5 + Tailwind CSS (CDN) + JavaScript vanilla |
| Backend | Python 3.12 + Django 5 + Django REST Framework |
| Base de datos | PostgreSQL (Railway) / SQLite (desarrollo local) |
| Despliegue | Railway |
| Servidor estático | WhiteNoise |

---

## Estructura del proyecto

```
UPGWebSite/
├── frontend/                  # Sitio estático (HTML + Tailwind CDN)
│   ├── index.html             # Página principal
│   ├── pages/
│   │   ├── carreras.html
│   │   └── contacto.html
│   └── assets/
│       ├── css/custom.css
│       ├── js/main.js
│       └── img/
├── backend/                   # API REST Django
│   ├── manage.py
│   ├── config/                # settings, urls, wsgi
│   ├── apps/
│   │   ├── contenido/         # Facultades, Carreras, Noticias
│   │   ├── contacto/          # Mensajes y solicitudes de inscripción
│   │   └── sugerencias/       # Sugerencias y reclamos
│   ├── requirements.txt
│   └── Dockerfile
└── railway.toml               # Configuración de despliegue
```

---

## Instalación local

### Requisitos previos
- Python 3.12+
- Git

### Backend

```bash
cd backend

# Crear entorno virtual
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux/Mac

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
# Editar .env — por defecto usa SQLite local (USE_SQLITE=True)

# Crear base de datos y aplicar migraciones
python manage.py makemigrations
python manage.py migrate

# Crear superusuario para el panel admin
python manage.py createsuperuser

# Iniciar servidor
python manage.py runserver 8001
```

API disponible en: `http://localhost:8001/api/`  
Panel admin: `http://localhost:8001/admin/`

### Frontend

```bash
cd frontend
python -m http.server 3000
```

Sitio disponible en: `http://localhost:3000`

---

## Endpoints de la API

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/contenido/facultades/` | Listado de facultades |
| GET | `/api/contenido/carreras/` | Carreras (filtrable por facultad, modalidad) |
| GET | `/api/contenido/noticias/` | Noticias publicadas |
| GET | `/api/contenido/pagina/<clave>/` | Contenido editable de página |
| POST | `/api/contacto/mensaje/` | Enviar mensaje de contacto |
| POST | `/api/contacto/solicitud/` | Solicitar información / inscripción |
| POST | `/api/sugerencias/sugerencia/` | Enviar sugerencia |
| POST | `/api/sugerencias/reclamo/` | Registrar reclamo |

---

## Despliegue en Railway

1. Crear un nuevo proyecto en [Railway](https://railway.app)
2. Agregar servicio PostgreSQL y copiar `DATABASE_URL`
3. Conectar este repositorio de GitHub
4. Configurar variables de entorno en Railway:
   ```
   SECRET_KEY=<clave-segura>
   DEBUG=False
   ALLOWED_HOSTS=<tu-dominio>.railway.app
   DATABASE_URL=<url-provista-por-railway>
   ```
5. Railway detecta `railway.toml` y despliega automáticamente

---

## Licencia

Este proyecto está licenciado bajo la [MIT License](LICENSE).  
Copyright © 2026 Ezequiel Alejandro Cristaldo Krechuk
