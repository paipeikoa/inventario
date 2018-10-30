from django import forms
from productos.models import Producto, Categoria
from django.core.validators import RegexValidator

class CategoriaForm(forms.ModelForm):
    nombre = forms.CharField(
        validators=[RegexValidator(r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]{1,50}$', "Ingrese nombre válido")])

    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']

        def __init__(self, *args, **kwargs):
            super(CategoriaForm, self).__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                        'class': 'form-control'
                    })


class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(
        validators=[RegexValidator(r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]{1,50}$', "Ingrese nombre válido")])

    class Meta:
        model = Producto
        fields = ['categoria','nombre', 'marca', 'tipo_producto', 'precio', 'cantidad','imagenes']

        def __init__(self, *args, **kwargs):
            super(ProductForm, self).__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                        'class': 'form-control'
                    })

