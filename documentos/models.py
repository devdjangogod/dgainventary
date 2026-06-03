from django.db import models
from django.utils import timezone

class Documento(models.Model):

    ESTADOS = [
        ('PENDIENTE', '🟡 Pendiente de salida'),
        ('DERIVADO', '🟢 Derivado'),
        ('ARCHIVADO', '🔵 Archivado'),
    ]
        
    TIPO_DOCUMENTO = [
        ('OFICIO', 'Oficio'),
        ('MEMORANDO', 'Memorando'),
        ('PROVEIDO', 'Proveído'),
        ('DICTAMEN', 'Dictamen'),
        ('RESOLUCION', 'Resolución'),
        ('OTRO', 'Otro'),
    ]

    # ENTRADA
    fecha_ingreso = models.DateField(default=timezone.now)
    numero_expediente = models.CharField(max_length=100)
    numero_registro_principal = models.CharField(max_length=100)
    numero_registro_adjunto = models.CharField(max_length=100, blank=True)
    autor = models.CharField(max_length=150)
    tipo_documento = models.CharField(max_length=50, choices=TIPO_DOCUMENTO)
    numero_documento = models.CharField(max_length=100)
    asunto = models.TextField()

    # SALIDA
    fecha_salida = models.DateField(null=True, blank=True)
    oficina_derivada = models.CharField(max_length=150, blank=True)
    firmo_jefe = models.BooleanField(default=False)
    link_drive = models.URLField(max_length=500, blank=True)

    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.tipo_documento} - {self.numero_documento}'
    

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='PENDIENTE'
    )


    numero_expediente = models.CharField(
        max_length=100,
        unique=True
    )

    numero_registro_principal = models.CharField(
        max_length=100,
        unique=True
    )