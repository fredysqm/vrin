from django.contrib import admin
from app.models import universidad, cargo, grado, participante

admin.site.register(universidad)
admin.site.register(cargo)
admin.site.register(grado)
admin.site.register(participante)