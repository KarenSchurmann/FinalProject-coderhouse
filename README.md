# Trabajo final-entrega intermedia
Para poder realizar el proyecto comence creando una carpeta en mi escritorio, llamada "Proyecto final-entrega intermedia". Una vez creada, puedo ingresar a VSC y crear mi proyecto dentro de la carpeta.
El command utilizado fue: django-admin startproject ProyectoFinal
Me paro en mi proyecto, con el command cd ProyectoFinal y realizo la migracion de datos para crear mi base de datos sqlite. Utilizo el command: python manage.py migrate

Creo mi app con el command: python manage.py startapp BioResearch.
La agrego a la lista de apps en settings.py 

Diseño de templates:
Dentro del proyecto creo un folder llamado "templates" y dentro del mismo un archivo .html (templates.html).
Dentro de este template, que sera el template "padre" voy a tipear mi esqueleto base. (html:5)
En el template padre voy a cargar mis statics, previamente descargados de bootstrap y guardados en la carpeta de mi proyecto. Diseñe mi template con una nav bar que posee un boton de search, un input group para forms, un index y una home principal. Luego voy a crear los templates "hijos" que van a heredar del padre.

En las views de mi aplicacion voy a crear tantas vistas como templates cree. Voy a definir mis vistas segun el modelos request-response. Voy a crear el contexto y el render.

Luego voy a ir a mi urls.py y escribir las rutas de mis views y el nombre con el que las voy a llamar.

Voy a cargar mi template desde Django utilizando la funcion loader.

Para crear el modelo voy a ingresar a models.py e importar los modelos de django.db
Luego voy a crear las diferentes clases de modelos que representan mis objetos.


