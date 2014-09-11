from django.contrib import admin
from .models import universidad, cargo, grado, participante, evento, asistencia

class universidad_admin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    list_editable = ('nombre',)
    search_fields = ('id', 'nombre',)

class cargo_admin(admin.ModelAdmin):
    list_display = ('id', 'nombre',)
    list_editable = ('nombre',)
    search_fields = ('id', 'nombre',)

class grado_admin(admin.ModelAdmin):
    list_display = ('id', 'nombre',)
    list_editable = ('nombre',)
    search_fields = ('id', 'nombre',)

class participante_admin(admin.ModelAdmin):
    list_display = ('dni', 'paterno', 'materno', 'nombre')
    list_editable = ('paterno', 'materno', 'nombre')
    search_fields = ('dni', 'paterno', 'materno', 'nombre')
    list_filter = ('grado', 'cargo')
    ordering = ['-ingreso']

class evento_admin(admin.ModelAdmin):
    list_display = ('id', 'nombre','fecha_hora','cerrado')
    list_editable = ('nombre',)
    search_fields = ('id','nombre',)

class asistencia_admin(admin.ModelAdmin):
    list_display = ('id', 'evento', 'participante', 'fecha_hora')
    list_filter = ('evento',)
    search_fields = ('evento__id', 'evento__nombre','participante__dni','participante__paterno',
        'participante__materno','participante__nombre')


admin.site.register(universidad, universidad_admin)
admin.site.register(cargo, cargo_admin)
admin.site.register(grado, grado_admin)
admin.site.register(participante, participante_admin)
admin.site.register(evento, evento_admin)
admin.site.register(asistencia, asistencia_admin)