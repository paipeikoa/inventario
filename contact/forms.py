from django import forms

class contactForm(forms.Form):
    name = forms.CharField(required=True, label=("Nombre"),
                           widget=forms.TextInput(
                           attrs={'placeholder': ('Juan Perez'),
                                  'autofocus': 'autofocus'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={'type': 'email',
               'placeholder':('ejemplo@mail.com')}))
    message = forms.CharField(required=True, label=("Mensaje"),widget=forms.Textarea(
    						  attrs={'placeholder': ('Escriba aquí su consulta'),
                              	     'autofocus': 'autofocus'}))

