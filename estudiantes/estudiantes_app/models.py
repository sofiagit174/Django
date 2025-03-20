# filepath: c:\Users\Danna\Downloads\CREAR\estudiantes\estudiantes_app\models.py
from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    correo = models.EmailField()

    def __str__(self):
        return self.nombre