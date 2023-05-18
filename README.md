# Django Skeleton

[![Django Version](https://img.shields.io/badge/django-4.1.7-brightgreen)](https://www.djangoproject.com/)

Django Skeleton es un proyecto base para iniciar el desarrollo de una aplicación web con Django, Docker, Postgres, Gunicorn y Nginx. 

## Prerequisitos

Antes de comenzar, debes tener instalado Docker y Docker Compose en tu sistema. Si no los tienes instalados, puedes descargarlos y obtener instrucciones de instalación en los siguientes enlaces oficiales:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Configuración

Antes de utilizar el proyecto, es necesario configurar las variables de entorno y los archivos de configuración de Docker Compose. Para ello, sigue los siguientes pasos:

1. Renombra los archivos `.env.dist` y `docker-compose.yaml.dist` a `.env` y `docker-compose.yaml`, respectivamente.
2. En el archivo `.env`, configura las variables de entorno para tu aplicación.
3. En el archivo `docker-compose.yaml`, configura los servicios de Docker para tu aplicación.

## Ejecución

Para ejecutar el proyecto, sigue los siguientes pasos:

1. Abre una terminal en la raíz del proyecto.
2. Ejecuta el comando `docker-compose up --build` para construir e iniciar los servicios de Docker. Agrega la opción `-d` para ejecutar en segundo plano.
3. Abre tu navegador y ve a la dirección http://localhost para ver la aplicación web.

## Migraciones y Superusuario

Para correr las migraciones y crear un superusuario en el contenedor de Django, sigue los siguientes pasos:

1. Ejecuta el comando `docker ps` para identificar el contenedor de Django.
2. Ejecuta el comando `docker exec -it <id_contenedor> /bin/sh` para ingresar al contenedor de Django.
3. Ejecuta los siguientes comandos dentro del contenedor:
    ```
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py createsuperuser --no-input
    ```
    
## Healtcheck

Al ingresar al proyecto se despliega automáticamente un servicio de healtcheck para verificar que el proyecto se encuentra operativo.

## Librerías y Estándares

El proyecto utiliza las siguientes librerías y dependencias:

- Django==4.1.7
- django-extensions==3.1.3
- gunicorn==20.1.0
- python-decouple==3.4
- psycopg2-binary==2.9.5
- djangorestframework==3.14.0
- django-crontab==0.7.1
- flake8==3.9.2
- black==22.10.0

Además, se utilizan las siguientes herramientas para cumplir con los estándares de PEP 8:

- [Flake8](https://flake8.pycqa.org/en/latest/)
- [Black](https://black.readthedocs.io/en/stable/)