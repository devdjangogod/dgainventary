from django.contrib import admin
from .models import Documento

@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = (
        'fecha_ingreso',
        'numero_expediente',
        'tipo_documento',
        'numero_documento',
        'autor',
        'oficina_derivada',
        'firmo_jefe',
    )

    search_fields = (
        'numero_expediente',
        'numero_documento',
        'autor',
        'asunto',
        'oficina_derivada',
    )

    list_filter = (
        'tipo_documento',
        'firmo_jefe',
        'fecha_ingreso',
        'fecha_salida',
    )