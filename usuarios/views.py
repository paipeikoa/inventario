from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import EditProfileForm,SignupForm, UserProfileEdit
from django.contrib import messages


# Create your views here.

def home(request):
    context = {}
    templates = 'home.html'
    return render(request,templates,context)

def about(request):
    context = {}
    templates = 'about.html'
    return render(request,templates,context)

@login_required
def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'profile.html', args)

@login_required
def edit_profile(request):
    data = {'telefono_fijo':request.user.userprofile.telefono_fijo,
            'telefono_movil':request.user.userprofile.telefono_movil,
            'edad':request.user.userprofile.edad,
            'fecha_nacimiento':request.user.userprofile.fecha_nacimiento,
            'direccion':request.user.userprofile.direccion,
            'localidad':request.user.userprofile.localidad,
            #'imagen':request.user.userprofile.imagen,
    }

    user_profile_form = EditProfileForm(request.POST or None, instance=request.user, initial=data)
    
    if request.method == 'POST':
        if user_profile_form.is_valid():
            print(data)
            user_profile_form.save(commit=True)      
            user_edit_form = UserProfileEdit(data=request.POST,instance=request.user.userprofile)
            user_edit_form.save(commit=True)
            messages.success(request,'Los cambios se guardaron éxito')
            return redirect(reverse('profile'))
    return render(request, 'edit-profile.html', context={'form':user_profile_form})
