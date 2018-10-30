from django import forms
from django.forms.models import modelformset_factory, inlineformset_factory
from productos.models import Producto, Proveedor, Compra, DetalleCompra, Categoria
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
    #imagenes = forms.FileField(
    #    label='Elija el archivo',
    #    help_text='max. 42 megabytes')

    class Meta:
        model = Producto
        fields = ['categoria','nombre', 'marca', 'tipo_producto', 'precio', 'cantidad','imagenes']

        def __init__(self, *args, **kwargs):
            super(ProductForm, self).__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                        'class': 'form-control'
                    })

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['proveedor_numero', 'razon_social', 'direccion', 'telefono','correo', 'estado']

    def __init__(self, *args, **kwargs):
        super(ProveedorForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            if field != 'estado':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })
                if field == 'proveedor_numero':
                    self.fields[field].widget.attrs.update(placeholder='102938')
                if field == 'razon_social':
                    self.fields[field].widget.attrs.update(placeholder='Grupo Dema S.R.L')
                if field == 'direccion':
                    self.fields[field].widget.attrs.update(placeholder='Av. Siempre Viva 2018')    
                if field == 'telefono':
                    self.fields[field].widget.attrs.update(placeholder='2614275058')
                if field == 'correo':
                    self.fields[field].widget.attrs.update(placeholder='ejemplo@mail.com')


class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['proveedor']

    def __init__(self, *args, **kwargs):
        super(CompraForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class DetalleCompraForm(forms.ModelForm):
    class Meta:
        model = DetalleCompra
        fields = ['producto', 'cantidad', 'precio_compra','total']

    def __init__(self, *args, **kwargs):
        super(DetalleCompraForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad == '':
            raise forms.ValidationError("Debe ingresar una cantidad valida")
        return cantidad

    def clean_precio_compra(self):
        precio = self.cleaned_data['precio_compra']
        if precio == '':
            raise forms.ValidationError("Debe ingresar un precio valido")
        return precio


DetalleCompraFormSet = inlineformset_factory(Compra, DetalleCompra, form=DetalleCompraForm, extra=1)


