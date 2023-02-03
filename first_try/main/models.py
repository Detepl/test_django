from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField("login",max_length=25)
    pasw = models.CharField("password",max_length=25)

    def __str__(self):
        return self.name
        return self.pasw

       