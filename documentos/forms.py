from django import forms
from django.utils import timezone
from .models import Documento

class EntradaDocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = [
            'numero_expediente',
            'numero_registro_principal',
            'numero_registro_adjunto',
            'autor',
            'tipo_documento',
            'numero_documento',
            'asunto',
        ]
        widgets = {
            'asunto': forms.Textarea(attrs={'rows': 3}),
        }


class SalidaDocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = [
            'fecha_salida',
            'oficina_derivada',
            'firmo_jefe',
            'link_drive',
        ]
        widgets = {
            'fecha_salida': forms.DateInput(
                attrs={
                    'type': 'date',
                    'value': timezone.now().date()
                }
            ),
        }