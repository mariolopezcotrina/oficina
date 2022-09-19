# Introduccion a Mysql

# Introduccion a django

## Instalamos Django y Django rest framework
```script
pip install django
pip install djangorestframework
```

## Vamos a crear nuestro proyecto
```script
django-admin startproject django_intro

django-admin startproject album .  ```para produccion```
```

## Ingresamos a la carpeta
```script
cd django_intro
album       ```para produccion```
```

## Para ejectutar mi servidor
```script
python manage.py runserver
```

## Para poder crear un superusuario necesitamos migrar
```script
python manage.py makemigrations
python manage.py migrate
```

## Para crear un superusuario
```script
python manage.py createsuperuser
```
p
## Creamos una aplicacion
```script
python manage.py startapp products
```

## Añadimos esta aplicacion en INSTALLED_APPS
```script
INSTALLED_APPS = [
    ...,
    'productos'
]
```

## Una vez creado mas modelos necesitamos migrar
```script
python manage.py makemigrations gestion --name agrege_tabla_usuarios
python manage.py migrate
python manage.py showmigrations
```


## agregar en settings
```
from dotenv import load_dotenv
from os import environ

load_dotenv()
```
## Para probar nuestra primera ruta de API añadirmos rest framework a INSTALLED_APPS
```script
INSTALLED_APPS = [
    ...,
    'rest_framework',
]
```