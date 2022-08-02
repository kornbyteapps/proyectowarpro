# Helpdesk Warpro

_Sistema de manejo de usuarios y tickets mediante APIREST en DJANGO REST FRAMEWORK_

## Clonar proyecto 🚀

_Para clonar el proyecto:_
```
git clone https://github.com/kornbyteapps/proyectowarpro.git
```

### Pre-requisitos 📋

_Para iniciar es necesario instalar la versión 3.9.13 de Python con Version Pip 22.2_

_Crear un entorno virtual para posteriormente activarlo _

``` python
$ python -m venv nombre_entorno
luego $ .\env\Scripts\activate
```

```
para instalar dependencias: 
$ pip install requirementes.txt
```

### Puesta a punto 🔧

_Una vez instalado lo anterior debemos proceder a configurar dentro del proyecto la base de datos que tengamos destinada para este fin_

-DEVELOP: Para iniciar el proyecto en develop debemos modificar el archivo LOCAL dentro de la carpeta Settings y añadir
los datos propios de nuestra base de datos_
``` python
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'hostname',
        'PORT': 'puerto',
        'USER':'usuario',
        'PASSWORD':'password',
        'NAME':'name_db',
        'OPTIONS':{
            'init_command':"SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
```
_Adicional añadir los hosts permnitidos para las requests en_
``` python
ALLOWED_HOSTS = ['examplelocalhost:8800']

```
_PRODUCTION: para iniciar el proyecto en producción debemos realizar el procedimiento anterior pero para el archivo PRODUCTION.PY dentro de la carpeta Settings_
_Es necesario ademas realizar cambios a los archivos Settings/base.py, wsgi.py, asgi.py ,manage.py
```python
En manage.py : os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tickets.settings.production)linea 9

En wsgi.py :os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tickets.settings.production)linea 14

En asgi.py :os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tickets.settings.production)linea 14

```

_Para el archivo Base modificar_

```python
ALLOWED_HOSTS = ['examplelocalhost:8800']
y pasar DEBUG = True a DEBUG = False

Setear adicionalmente el tiempo de vida para los tokens JWT use y refresh 
SIMPLE_JWT={
    'ACCES_TOKEN_LIFETIME':timedelta(hours=120),
    'REFRESH_TOKEN_LIFETIME':timedelta(hours=120),
    'ROTATE_REFRESH_TOKENS':True,
    'BLACKLIST_AFTER_ROTATION':True

}
```

_Una vez configurado lo anterior, procederemos a ejecutar las migraciones correspondientes de la siguiente forma_

## Para las migraciones ⚙️

_En la consola y dentro de la carpeta principal del proyecto ejecutar_

```
$ python manage.py makemigrations

luego
$ python manage.py migrate

Creamos un super usuario con
$ python manage.py createsuperuser

Finalmente corremos el servidor con
$ python manage.py runserver
```
### Analice las pruebas end-to-end 🔩

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

### Para la documentación añadida del proyecto una vez corriendo dirigirse a la dirección local en la que esté corriendo el servidor /docu, ej:http://127.0.0.1:8000/docu/ 

para detalles sobre modelos creados con el ORM de DRF dirigirse a la carpeta apps/nombreapp/models.py⌨️


## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [Django Rest Frameowrk](Oficial:https://www.django-rest-framework.org
external: https://www.cdrf.co) - El framework web usado
* [Maven](https://maven.apache.org/) - Manejador de dependencias
* [ROME](https://rometools.github.io/rome/) - Usado para generar RSS

## Contribuyendo 🖇️

Por favor lee el [CONTRIBUTING.md](https://gist.github.com/villanuevand/xxxxxx) para detalles de nuestro código de conducta, y el proceso para enviarnos pull requests.

## Wiki 📖

Puedes encontrar mucho más de cómo utilizar este proyecto en nuestra [Wiki](https://github.com/tu/proyecto/wiki)

## Versionado 📌

Usamos [SemVer](http://semver.org/) para el versionado. Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/tu/proyecto/tags).

## Autoresa ✒️

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **Andrés Villanueva** - *Trabajo Inicial* - [villanuevand](https://github.com/villanuevand)
* **Fulanito Detal** - *Documentación* - [fulanitodetal](#fulanito-de-tal)

También puedes mirar la lista de todos los [contribuyentes](https://github.com/your/project/contributors) quíenes han participado en este proyecto. 

## Licencia 📄

Este proyecto está bajo la Licencia (Tu Licencia) - mira el archivo [LICENSE.md](LICENSE.md) para detalles

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 o un café ☕ a alguien del equipo. 
* Da las gracias públicamente 🤓.
* Dona con cripto a esta dirección: `0xf253fc233333078436d111175e5a76a649890000`
* etc.



---
⌨️ con ❤️ por [Villanuevand](https://github.com/Villanuevand) 😊
