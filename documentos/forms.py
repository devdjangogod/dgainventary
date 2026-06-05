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



class DocumentoForm(forms.ModelForm):
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['numero_documento'].widget.attrs.update({
            'readonly': True,
            'class': 'form-control bg-light fw-bold'
        })




from django import forms
from .models import ReservaDocumento

class ReservaDocumentoForm(forms.ModelForm):
    class Meta:
        model = ReservaDocumento
        fields = ['tipo_documento', 'numero_documento', 'autor']

        widgets = {
            'tipo_documento': forms.Select(attrs={'class': 'form-select'}),
            'numero_documento': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.Select(attrs={'class': 'form-select'}),
        }