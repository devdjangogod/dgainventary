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

    fecha_ingreso = models.DateField(default=timezone.now)

    numero_expediente = models.CharField(max_length=100, unique=True)
    numero_registro_principal = models.CharField(max_length=100, unique=True)
    numero_registro_adjunto = models.CharField(max_length=100, blank=True)

    autor = models.CharField(max_length=150)
    tipo_documento = models.CharField(max_length=50, choices=TIPO_DOCUMENTO)

    numero_documento = models.CharField(max_length=30, blank=True)

    asunto = models.TextField()

    fecha_salida = models.DateField(null=True, blank=True)
    oficina_derivada = models.CharField(max_length=150, blank=True)
    firmo_jefe = models.BooleanField(default=False)
    link_drive = models.URLField(max_length=500, blank=True)

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='PENDIENTE'
    )

    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.tipo_documento} - {self.numero_documento}'

    def save(self, *args, **kwargs):
        if not self.numero_documento:
            ultimo = Documento.objects.filter(
                tipo_documento=self.tipo_documento
            ).order_by('-id').first()

            if ultimo and ultimo.numero_documento:
                try:
                    ultimo_numero = ultimo.numero_documento.split('-')[-1]
                    correlativo = int(ultimo_numero) + 1
                except:
                    correlativo = 1
            else:
                correlativo = 1

            self.numero_documento = str(correlativo).zfill(3)

        super().save(*args, **kwargs)