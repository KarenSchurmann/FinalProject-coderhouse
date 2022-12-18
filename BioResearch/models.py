from django.db import models

# Create your models here.

class Title(models.Model):
   title = models.CharField(max_length=200)
   subtitle = models.CharField(max_length=100, default='' )

def __str__(self) -> str :
    return f"{self.title}"
   
class Theme(models.Model):
    main_theme = models.CharField(max_length=100)

def __str__(self) -> str :
    return f"{self.main_theme}"

class Authors(models.Model):
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)

def __str__(self) -> str:
        return f"{self.last_name} {self.first_name}"

class Language(models.Model):
    language = models.CharField(max_length=50)

def __str__(self) -> str:
    return f"{self.language}"

class Published(models.Model):
    pub_date = models.DateField('Date published')


class Access(models.Model):
    open_access =  models.BooleanField()



