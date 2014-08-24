from django.db import models


class universidad(models.Model):
    nombre = models.CharField(max_length=140)


class cargo(models.Model):
    nombre = models.CharField(max_length=60)


class grado(models.Model):
    nombre = models.CharField(max_length=60)


class participante(models.Model):
    dni = models.CharField(max_length=8, unique=True)
    paterno = models.CharField(max_length=80)
    materno = models.CharField(max_length=80)
    nombre = models.CharField(max_length=100)
    edad = models.SmallIntegerField()
    direccion = models.CharField(max_length=140)
    email = models.EmailField()
    fijo = models.BigIntegerField()
    movil = models.BigIntegerField()

    universidad = models.ForeignKey(universidad)
    facultad = models.CharField(max_length=140)
    carrera = models.CharField(max_length=140)
    titulo = models.CharField(max_length=140)
    cargo = models.ForeignKey(cargo)
    grado = models.ForeignKey(grado)

    investigacion = models.TextField()