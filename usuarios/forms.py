from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.forms import User
from django import forms
from django.contrib import messages

class SignupForm(forms.ModelForm):
	first_name = forms.CharField(max_length=45, required=True,
							label=("Nombre"),widget=forms.TextInput(
                            attrs={'placeholder': ('Juan'),
                                  'autofocus': 'autofocus'}))
	last_name = forms.CharField(max_length=45, required=True,
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
	telefono_fijo = forms.CharField(max_length=11, required=False,
							label=("Teléfono Fijo"),widget=forms.TextInput(
                            attrs={'placeholder': ('2614275058'),
                                  'autofocus': 'autofocus'}))
	telefono_movil = forms.CharField(max_length=11, required=False,
							label=("Teléfono Móvil"),widget=forms.TextInput(
                            attrs={'placeholder': ('2616133576'),
                                  'autofocus': 'autofocus'}))
	edad = forms.CharField(max_length=2, required=False,
							label=("Edad"),widget=forms.TextInput(
                            attrs={'placeholder': ('18'),
                                  'autofocus': 'autofocus'}))
	fecha_nacimiento = forms.DateField(widget=forms.SelectDateWidget(),
               label='Fecha de Nacimiento')

    provincia = forms.CharField(widget=forms.Select(choices=PROVINCIAS))


	class Meta:
		model = User
		fields = ['first_name','last_name','email',
				  'telefono_fijo','telefono_movil',
				  'edad','fecha_nacimiento']

class UserProfileEdit(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['telefono_fijo','telefono_movil',
				  'edad','fecha_nacimiento']