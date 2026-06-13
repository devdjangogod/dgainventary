from django import forms
from .models import Trabajador

class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields = [
            'usuario',
            'dni',
            'sede',
            'local',
            'dependencia',
            'unidad',
            'area',
            'sub_area',
            'ambiente',
            'piso',
            'referencia',
            'activo',
        ]