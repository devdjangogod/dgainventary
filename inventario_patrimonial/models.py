from django.db import models


class BienInventario(models.Model):
    usuario_responsable = models.CharField(max_length=150, blank=False, null=False)
    dni = models.CharField(max_length=20, blank=False, null=False)
    sede_filial = models.CharField(max_length=100, blank=False, null=False)
    local = models.CharField(max_length=150, blank=True, null=True)
    dependencia = models.CharField(max_length=150, blank=True, null=True)
    unidad_nivel_1 = models.CharField(max_length=150, blank=True, null=True)
    area_nivel_2 = models.CharField(max_length=150, blank=True, null=True)
    sub_area_nivel_3 = models.CharField(max_length=150, blank=True, null=True)
    nombre_ambiente = models.CharField(max_length=150, blank=True, null=True)
    piso_nivel = models.CharField(max_length=50, blank=True, null=True)
    referencia_ubicacion = models.TextField(blank=True, null=True)

    cod_inv_2025 = models.CharField(max_length=100, blank=True, null=True)
    codigo_patrimonial_conciliado = models.CharField(max_length=100, blank=True, null=True)

    descripcion = models.TextField()
    marca = models.CharField(max_length=100, blank=True, null=True)
    modelo = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=80, blank=True, null=True)
    serie = models.CharField(max_length=100, blank=True, null=True)
    dimensiones = models.CharField(max_length=150, blank=True, null=True)

    s_1 = models.CharField(max_length=50, blank=True, null=True)
    e_2 = models.CharField(max_length=50, blank=True, null=True)

    observacion = models.TextField(blank=True, null=True)

    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descripcion