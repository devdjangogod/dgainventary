from django import forms
from .models import BienInventario
from trabajadores.models import Trabajador


class BienInventarioForm(forms.ModelForm):

    usuario_responsable = forms.ModelChoiceField(
        queryset=Trabajador.objects.all(),
        empty_label="Seleccione trabajador",
        required=True,
        label="Usuario Responsable",
        widget=forms.Select(attrs={
            "class": "form-select"
        })
    )

    class Meta:
        model = BienInventario
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.is_bound:  # cuando se envía el formulario

            for campo in self.errors:

                widget = self.fields[campo].widget

                css = widget.attrs.get("class", "")

                if "is-invalid" not in css:
                    widget.attrs["class"] = f"{css} is-invalid"