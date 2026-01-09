# prueba-tecnica-CALA
Prueba tecnica CALA analytics.

## Pasos para ejecutar el proyecto
- Asegura Python 3.12+ y crea el entorno virtual: `python -m venv .venv`
- Activa el entorno: `source .venv/bin/activate` (Linux/Mac) o `.venv\Scripts\activate` (Windows)
- Instala Django: `pip install django`
- ingresa al directorio del proyecto: `cd analytics_portal`
- Ejecuta migraciones: `python manage.py migrate`
- Levanta el servidor: `python manage.py runserver`

## Decisiones técnicas tomadas
- Se incluyo el app core para manejar la vista principal de la aplicación como un home page e incluir los endpoints para navegar
por la aplicaión.
- Se incluyo el modelo de datos del bloque 2 para demostrar la parte 2 del bloque 2.

## Principales aprendizajes
 - Mi principal aprendizaje fue en la parte de la creación de las vistas HTML de la aplicación y en la parte de la creación de los endpoints sin usar el framework de Django REST Framework.
