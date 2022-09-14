Aquí haremos una api rest con Django usando el curso que me paso Lecks de Oreilly

los primeros videos son mucha introducción y repaso y aquí empieza la creación
https://learning.oreilly.com/videos/build-rest-apis/9781801819022/9781801819022-video3_1/


empezamos inicializando nuestro git
``git init``

seguimos con nuestro entorno virtual 

``virtualenv -p python env``

y lo activamos

``.\env\Scripts\activate``

ahora instalamos Django

``pip install django``

luego iniciamos un proyecto en Django con el siguiente comando

``django-admin startproject watchmate .``

el punto del final es muy importante para que no me haga el cagadero de siempre de carpetas y con esto solo creamos una carpeta y entrando esta todo

![[Pasted image 20220913173244.png]]

ahora nos crearemos nuestra app (no api aun)
``python manage.py startapp watchlist_app``

como buena practica el del video le pone  ``_app``  para diferenciar entre el proyecto principal y las app's que hagamos, vamos a settings.py y ponemos nuestra app, si no tendremos errores al hacer las migraciones (cosa que me paso a mi)
![[Pasted image 20220913183040.png]]

corremos el servidor con 
``python manage.py runserver``

![[Pasted image 20220913175113.png]]


con esto hecho ahora hacemos las migraciones
``python manage.py migrate``

y después creamos nuestro superusuario
``python manage.py createsuperuser``

ahora vamos a la área de administración y nos logeamos

![[Pasted image 20220913175616.png]]


vamos a nuestra carpeta de watchlist_app y creamos un archivo urls.py

y siguiendo la arquitectura de Django también vamos a models para declarar la siguiente clase

```
from django.db import models

  

# Create your models here.

class Movie(models.Model):

    name = models.CharField(max_length=50)

    description = models.CharField(max_length=200)

    active = models.BooleanField(default=True)

  

    def __str__(self):

        return self.name
```

creando esto hacemos las migraciones nuevamente
``python manage.py makemigrations``
``python manage.py migrate``

ahora vamos a admin.py y declaramos nuestro modelo que creamos en models, tenemos que importarlo primero

```
from django.contrib import admin

from watchlist_app .models import Movie

  

# Register your models here.

admin.site.register(Movie)
```

ahora si actualizamos el sitio de administración veremos esto

![[Pasted image 20220913183404.png]]

dentro registramos dos películas para practicar
![[Pasted image 20220913183617.png]]

ahora vamos a views.py par crear nuestras vistas
```
from django.shortcuts import render

from watchlist_app.models import Movie

  

def movie_list(request):

    movies = Movie.objects.all()

    print(movies)
```

con esto estamos instanseando muestro objeto movies y le ponemos un print para que nos sirva al ver la consola casa que se llame

vamos a watchmate/urls.py y declaramos que use esa vista

```
from django.contrib import admin

from django.urls import path, include

  

urlpatterns = [

    path('admin/', admin.site.urls),

    path('movie/', include('watchlist_app.urls')),

]
```

y leugo vamos a watchlist_app/urls.py y ponemos lo siguiente

```
from django.urls import path, include

from watchlist_app.views import movie_list

  

urlpatterns = [

    path('list/', movie_list, name='movie-list'),

]
```


ahora en nuestra vista, la modificamos para que nos muestre un Json (aqui se enredo muchiiiiiisimo y tubo un monton de errores tuve que regresar y editar los archivos ruls.py)

```
from django.shortcuts import render

from watchlist_app.models import Movie

from django.http import JsonResponse

  

def movie_list(request):

    movies = Movie.objects.all()

    data = {'movies':

        list(movies.values())

        }

    return JsonResponse(data)
```

vamos a http://127.0.0.1:8000/movie/list/

![[Pasted image 20220913185934.png]]

# Llegamos al final del video
https://learning.oreilly.com/videos/build-rest-apis/9781801819022/9781801819022-video3_4/