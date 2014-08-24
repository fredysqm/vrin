from django.db import models


class participante(models.Model):
    dni = models.CharField(max_length=8, unique=True)
    paterno = models.CharField(max_length=80)
    materno = models.CharField(max_length=80)
    nombre = models.CharField(max_length=100)
    edad = models.SmallIntegerField()
    direccion = models.CharField(max_length=140)
    email = models.EmailField()
    fijo = models.
    movil = models.


    def __unicode__(self):
        return "Persona %s" % (self.dni)