import token
from django.db import models

# Create your models here.

#Modelo que representa a los papers
class Paper(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=100)
    main_theme = models.TextField()
    link = models.URLField(default='')
    authors = models.TextField(default='')
    published_date = models.DateField ()
    open_access =  models.BooleanField()

    def __str__(self) -> str :
        return f"{self.open_access} \n {self.title} ({self.published_date}) \n {self.subtitle} \n {self.authors} \n {self.main_theme}"


class MainTheme(models.Model):
    main_theme = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return f"{self.main_theme}"

#Modelo Author

class Author(models.Model):
    #Modelo que representa a los autores 
    name = models.TextField(default='')
    collaborations = models.TextField()

    def __str__(self) -> str:
        return f"{self.name} \n {self.collaborations}"


class NewPaper(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=100)
    main_theme = models.TextField(default='')
    authors = models.TextField(default='')
    published_date = models.DateField ()
    open_access =  models.BooleanField()

    def __str__(self) -> str :
        return f"{self.open_access} \n {self.title} ({self.published_date}) \n {self.subtitle} \n {self.authors} \n {self.main_theme}"

class SearchPaper(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=100)
    main_theme = models.TextField(default='')
    authors = models.TextField(default='')
    published_date = models.DateField ()
    open_access =  models.BooleanField()

    def __str__(self) -> str :
        return f" {self.open_access} \n {self.title} ({self.published_date}) \n {self.subtitle} \n {self.authors} \n {self.main_theme}"

class Home(models.Model):
    welcome = models.TextField()

    def __str__(self) -> str:
        return f"{self.welcome}"