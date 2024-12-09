from django.db import models


# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()
    
    def __str__(self):
        return f"Nombre del curso: {self.nombre} - Numero de comision: {self.comision}"


class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()


class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)


class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_de_Entrega = models.DateField()
    entregado = models.BooleanField()
