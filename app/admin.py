from django.contrib import admin
from app.models import universidad, cargo, grado, participante

class universidad_admin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    list_editable = ('nombre',)
    search_fields = ('nombre',)

class cargo_admin(admin.ModelAdmin):
    list_display = ('id', 'nombre',)
    list_editable = ('nombre',)
    search_fields = ('nombre',)

class grado_admin(admin.ModelAdmin):
    list_display = ('id', 'nombre',)
    list_editable = ('nombre',)
    search_fields = ('nombre',)

class participante_admin(admin.ModelAdmin):
    list_display = ('dni', 'paterno', 'materno', 'nombre')
    list_editable = ('paterno', 'materno', 'nombre')
    search_fields = ('dni', 'paterno', 'materno', 'nombre')
    list_filter = ('grado', 'cargo')

admin.site.register(universidad, universidad_admin)
admin.site.register(cargo, cargo_admin)
admin.site.register(grado, grado_admin)
admin.site.register(participante, participante_admin)