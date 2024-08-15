from django.db import models

class Usuario(models.Model):
    Usuario = models.CharField(max_length=50)
    Senha = models.CharField(max_length=50)