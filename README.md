# Trabajo final-entrega intermedia
Para poder realizar el proyecto comence creando una carpeta en mi escritorio, llamada "Proyecto final-entrega intermedia". Una vez creada, puedo ingresar a VSC y crear mi proyecto dentro de la carpeta.
El command utilizado fue: django-admin startproject ProyectoFinal
Cuando hice eso entre a mi cuenta de git y cree un nuevo repositorio. Agregue mi proyecto al repo.
Me paro en mi proyecto, con el command cd ProyectoFinal y realizo la migracion de datos para crear mi base de datos sqlite. Utilizo el command: python manage.py migrate

Creo mi app con el command: python manage.py startapp BioResearch.
La agrego a la lista de apps en settings.py 

Diseño de templates:
Dentro del proyecto creo un folder llamado "templates" y dentro del mismo un archivo .html (templates.html).
Dentro de este template, que sera el template "padre" voy a tipear mi esqueleto base. (html:5)

templates-desarrollo web:
En el template padre voy a cargar mis statics, previamente descargados de bootstrap y guardados en la carpeta de mi proyecto. Diseñe mi template con una nav bar que posee un boton de search, un input group para forms, un index y una home principal. Luego voy a crear los templates "hijos" que van a heredar del padre.

views:
En las views de mi aplicacion voy a crear tantas vistas como templates cree. Voy a definir mis vistas segun el modelos request-response. Voy a crear el contexto y el render. Mis vistas van a hacer render de los templates.
En el caso de la vista que corresponda a agregar nuevo paper, voy a hacerlo a traves de un formulario. 


urls:
Luego voy a ir a mi urls.py y escribir las rutas de mis views y el nombre con el que las voy a llamar.

Voy a cargar mi template desde Django utilizando la funcion loader.

modelos:
Para crear el modelo voy a ingresar a models.py e importar los modelos de django.db
Luego voy a crear las diferentes clases de modelos que representan mis objetos.

admin: 
Importe mis modelos y los registro.

En la consola creo con python manage.py createsuperuser un usuario, contraseña y mail.
A traves del site, seccion admin, voy a poder editar aspectos de los usuarios, papers agregados y tambien agregarlos.

forms:
cree un archivo en mi proyecto "forms.py" donde importe todos los forms. Cree clase.



