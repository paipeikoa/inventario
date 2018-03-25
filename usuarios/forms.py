from direcciones.models import Pais, Provincia, Localidad
from .models import UserProfile
from django.contrib.auth.forms import User
from django import forms
from django.core.validators import RegexValidator


class SignupForm(forms.ModelForm):
	first_name = forms.CharField(validators=[RegexValidator(r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]{1,30}$', "Ingrese nombre válido")],
							max_length=45, required=True,
							label=("Nombre"),widget=forms.TextInput(
                            attrs={'placeholder': ('Juan'),
                                  'autofocus': 'autofocus'}))
	last_name = forms.CharField(validators=[RegexValidator(r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]{1,30}$', "Ingrese apellido válido")],
							max_length=45, required=True,
							label=("Apellido"),widget=forms.TextInput(
                            attrs={'placeholder': ('Perez'),
                                  'autofocus': 'autofocus'}))
	
	class Meta:
		model = User
		fields = ['first_name', 'last_name']

	def signup(self, request, user):
		user.first_name = self.cleaned_data['first_name'].capitalize()
		user.last_name = self.cleaned_data['last_name'].capitalize()
		user.save()


class EditProfileForm(forms.ModelForm):

	first_name = forms.CharField(validators=[RegexValidator(r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]{1,30}$', "Ingrese nombre válido")],
							max_length=30, required=True,
							label=("Nombre"),widget=forms.TextInput(
                            attrs={'placeholder': ('Juan'),
                                  'autofocus': 'autofocus',
                                  'required':True}))
	last_name = forms.CharField(validators=[RegexValidator(r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]{1,30}$', "Ingrese apellido válido")],
							max_length=30, required=True,
							label=("Apellido"),widget=forms.TextInput(
                            attrs={'placeholder': ('Perez'),
                                  'autofocus': 'autofocus',
                                  'required':True}))
	telefono_fijo = forms.CharField(validators=[RegexValidator(r'^[0-9]{1,11}$', "Ingrese un número de teléfono válido sin guiones ej. 2614275058")],
							max_length=11, required=False,
							label=("Teléfono Fijo"),widget=forms.TextInput(
                            attrs={'placeholder': ('2614275058'),
                                  'autofocus': 'autofocus'}))
	telefono_movil = forms.CharField(validators=[RegexValidator(r'^[0-9]{1,11}$', "Ingrese un número de teléfono válido sin guiones ej. 2616133576")],
							max_length=11, required=False,
							label=("Teléfono Móvil"),widget=forms.TextInput(
                            attrs={'placeholder': ('2616133576'),
                                  'autofocus': 'autofocus'}))
	edad = forms.CharField(validators=[RegexValidator(r'^[1-9]{2}$', "Ingrese un número de edad válido, ej. 45")],
							max_length=2, required=False,
							label=("Edad"),widget=forms.TextInput(
                            attrs={'placeholder': ('18'),
                                  'autofocus': 'autofocus'}))
	fecha_nacimiento = forms.DateField(required=True,label='Fecha de Nacimiento',
							widget=forms.DateInput(attrs={'placeholder':'24/10/1986',
								  'required':True}))
	
	direccion = forms.CharField(validators=[RegexValidator(r'^[a-zA-Z0-9ñÑáéíóúÁÉÍÓÚ\.\s]{1,200}$', "Ingrese una dirección válida")],
							max_length=200, required=True,
							label=("Dirección"),widget=forms.TextInput(
                            attrs={'placeholder': 'San Juan 852',
                                  'autofocus': 'autofocus',
                                  'required':True}))

	
	localidad = forms.ModelChoiceField(queryset=Localidad.objects.all())
	
	#provincia = forms.ModelChoiceField(queryset=Provincia.objects.all())

	#departamento = forms.ModelChoiceField(queryset=Departamento.objects.all()) 

	class Meta:
		model = User
		fields = ['username','first_name','last_name','email',
				  'telefono_fijo','telefono_movil','edad',
				  'fecha_nacimiento','direccion','localidad']
				 

class UserProfileEdit(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['telefono_fijo','telefono_movil',
				  'edad','fecha_nacimiento','direccion',
				  'localidad']
