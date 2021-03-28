# Flask-Mongo-2256

Es proyecto requiere lo siguiente

- Flask
- MongoDB Atlas
- Pymongo

## Configuración

Lo que debemos hacer es crear un entorno virtual y activarlo. Luego de instalar todas las dependencias del proyecto generamos el archivo requirements que nos servirá para instalar todas las librerias cuando clonamos el repositorio desde cero.

```sh
$ virtualenv venv
$ source venv/bin/activate
$ pip freeze > requirements.txt
$
```

Luego instalamos las dependencias

```sh
$ pip install -r requirements.txt
```

### GCloud

Nuestro proyecto debe contar con un archivo app.yaml y el archivo principal del proyecto debe llamarse main.py

Primero, tenemos que iniciar sesion con nuestra cuenta de google. Si creemos conveniente podemos actualizar los componentes.

```sh
$ gcloud auth login
$ gcloud components update
$ 
```

Segundo, si queremos cambiar de projecto debemos primero listarlo para identificar su project_id para poder setearlo.

```sh
$ gcloud projects list
$ gcloud config set project PROJECT_ID
$ 
```

Cuando creamos un projecto por primera con en App Engine tenemos que seleccionar una region

```sh
$ gcloud app create
```

Finalmente, si todo ha sido correcto podemos proceder con el despliegue

```sh
$ gcloud app deploy
```