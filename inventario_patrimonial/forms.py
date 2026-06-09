from django import forms
from .models import BienInventario


class BienInventarioForm(forms.ModelForm):
    class Meta:
        model = BienInventario
        fields = "__all__"
        exclude = ["creado"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            css = "form-control"

            if self.errors.get(name):
                css += " is-invalid"

            field.widget.attrs.update({
                "class": css
            })