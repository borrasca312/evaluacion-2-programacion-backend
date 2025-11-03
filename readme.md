## Mesa de Ayuda – Django

Aplicación simple de Mesa de Ayuda donde usuarios autenticados pueden crear, listar, ver, editar, cerrar y eliminar solicitudes. Incluye categorías, prioridades y comentarios.

### Requerimientos
- Python 3.10+
- Pip

### Instalación (Windows PowerShell)
1. Clonar o abrir este proyecto.
2. Crear entorno virtual y activarlo:
	- python -m venv .venv
	- .\.venv\Scripts\Activate.ps1
3. Instalar dependencias:
	- pip install -r requirements.txt
4. Configurar variables de entorno:
	- Copia `.env.example` a `.env` y coloca un valor seguro para `DJANGO_SECRET_KEY`.
5. Aplicar migraciones y crear usuario:
	- python manage.py migrate
	- python manage.py createsuperuser

### Ejecutar
- python manage.py runserver

Luego visita: http://127.0.0.1:8000/

Rutas principales:
- /accounts/login/ – Iniciar sesión
- /accounts/registro/ – Registro
- /solicitudes/ – Lista de solicitudes

### Funcionalidades
- Autenticación: login, logout y registro (django.contrib.auth)
- CRUD Solicitudes: crear, listar (filtros por estado/categoría/búsqueda), detalle, editar, cerrar y eliminar (solo creador)
- Comentarios en solicitudes
- Validaciones en formularios (servidor)
- Templates con herencia y CSRF
- Admin de Django para gestionar modelos

### Seguridad y desarrollo
- Este proyecto está configurado para entorno local (DEBUG=True).
- En producción debes:
  - Definir `DJANGO_SECRET_KEY` y `DJANGO_ALLOWED_HOSTS` en variables de entorno
  - Activar cookies seguras y ajustar `DEBUG=False`

### Demo rápida
Tras crear el superusuario, inicia sesión y crea tus categorías en /admin/. Luego podrás crear solicitudes desde /solicitudes/.
