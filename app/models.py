# -*- coding: utf-8 -*-

from django.db import models

class slink(models.Model):
    keyword = models.CharField(max_length=140)
    def __unicode__(self): return "%s" % (self.nombre)

    class Meta:
        verbose_name = ('universidad')
        verbose_name_plural = ('universidades')

class cargo(models.Model):
    nombre = models.CharField(max_length=60)
    def __unicode__(self): return "%s" % (self.nombre)

class grado(models.Model):
    nombre = models.CharField(max_length=60)
    def __unicode__(self): return "%s" % (self.nombre)

class participante(models.Model):
    dni = models.CharField(max_length=8, primary_key=True, verbose_name="DNI")
    paterno = models.CharField(max_length=80, verbose_name="Apellido Paterno")
    materno = models.CharField(max_length=80, verbose_name="Apellido Materno")
    nombre = models.CharField(max_length=100, verbose_name="Nombre(s)")
    edad = models.SmallIntegerField(verbose_name="Edad", blank=True)
    direccion = models.CharField(max_length=140, verbose_name="Dirección")
    email = models.EmailField(verbose_name="Email")
    fijo = models.CharField(max_length=12, verbose_name="Teléfono Fijo",blank=True)
    movil = models.CharField(max_length=12, verbose_name="Teléfono Movil",blank=True)
    universidad = models.ForeignKey(universidad, verbose_name="Universidad")
    facultad = models.CharField(max_length=140, verbose_name="Facultad")
    carrera = models.CharField(max_length=140, verbose_name="Carrera")
    titulo = models.CharField(max_length=140, verbose_name="Título",blank=True)
    cargo = models.ForeignKey(cargo, verbose_name="Cargo")
    grado = models.ForeignKey(grado, verbose_name="Grado")
    investigacion = models.TextField(verbose_name="Trabajos de Investigación", blank=True)
    ingreso = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return u"(%s) %s-%s-%s" % (self.dni, self.paterno, self.materno, self.nombre)

    def save(self):
        self.paterno = self.paterno.upper()
        self.materno = self.materno.upper()
        self.nombre = self.nombre.upper()
        self.direccion = self.direccion.upper()
        self.email = self.email.lower()
        self.facultad = self.facultad.upper()
        self.carrera = self.carrera.upper()
        self.titulo = self.titulo.upper()
        if self.edad is None: self.edad = 0
        super(participante, self).save()

class evento(models.Model):
    nombre = models.CharField(max_length=60)
    cerrado = models.BooleanField(default=False)
    fecha_hora = models.DateTimeField()
    def __unicode__(self): return "%s" % (self.nombre)

class asistencia(models.Model):
    evento = models.ForeignKey(evento, verbose_name='Evento')
    participante  = models.ForeignKey(participante, verbose_name='Participante')
    fecha_hora = models.DateTimeField(auto_now=True)
    def __unicode__(self): return u"%s - %s" % (self.evento, self.participante)

    class Meta:
        unique_together = ('evento', 'participante',)
