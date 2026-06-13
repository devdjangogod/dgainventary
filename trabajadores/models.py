from django.db import models

class Trabajador(models.Model):

    usuario = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )

    dni = models.CharField(max_length=8, unique=True)

    sede = models.CharField(max_length=150, blank=True, null=True)
    local = models.CharField(max_length=150, blank=True, null=True)

    dependencia = models.CharField(max_length=150, blank=True, null=True)
    unidad = models.CharField(max_length=150, blank=True, null=True)

    area = models.CharField(max_length=150, blank=True, null=True)
    sub_area = models.CharField(max_length=150, blank=True, null=True)

    ambiente = models.CharField(max_length=150, blank=True, null=True)
    piso = models.CharField(max_length=50, blank=True, null=True)

    referencia = models.TextField(blank=True, null=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.usuario