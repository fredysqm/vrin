from django.db import models


class Docente(models.Model):
    usuario = models.OneToOneField(User, primary_key=True)

    def __unicode__(self):
        return "%s" % (User.username)


class Alumno(models.Model):
    usuario = models.OneToOneField(User, primary_key=True)

    def __unicode__(self):
        return "%s" % (User.username)


class Curso(models.Model):
    nombre = models.CharField(max_length=140)
    maestro = models.ForeignKey(Docente)
    fecha = models.DateField(auto_now=True)
    abierto = models.BooleanField(default=True)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return "Curso %s - %s" % (self.nombre, self.activo)


class Tema(models.Model):
    nombre = models.CharField(max_length=140)
    curso = models.ForeignKey(Curso)

    def __unicode__(self):
        return "%s" % (self.nombre)


class Matricula(models.Model):
    alumno = models.ForeignKey(Alumno)
    curso = models.ForeignKey(Curso)

    def __unicode__(self):
        return "%s - %s", (self.alumno.usuario, self.curso.nombre)


class ModeloExamen(models.Model):
    nombre = models.CharField(max_length=80)


class Examen(models.Model):
    examen = models.ForeignKey(ModeloExamen)
    fecha = models.DateTimeField()
    duracion = models.IntegerField(default=1800)
    rendido = models.BooleanField(default=False)


class Pregunta(models.Model):
    MAYBECHOICE = (
        ('F', 'Facil'),
        ('N', 'Normal'),
        ('D', 'Dificil'),
    )
    tema = models.ForeignKey(Tema)
    enunciado = models.CharField(max_length=1024)
    nivel = models.CharField(max_length=1, choices=MAYBECHOICE, default='N')

    def __unicode__(self):
        return "%s <> %s" % (self.tema.nombre, self.enunciado)


class Alternativa(models.Model):
    pregunta = models.ForeignKey(Pregunta)
    correcta = models.BooleanField(default=False)
    detalle = models.CharField(max_length=80)


class Respuesta(models.Model):
    alumno = models.ForeignKey(Alumno)
    examen = models.ForeignKey(Examen)
    alternativa = models.ForeignKey(Alternativa)


class Puntaje(models.Model):
    examen = models.ForeignKey(ModeloExamen)
    pregunta = models.ForeignKey(Pregunta)
    valor = models.IntegerField(default=1)
