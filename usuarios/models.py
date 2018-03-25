# Create your models here.
from django.contrib.contenttypes.fields import GenericRelation
from django.conf import settings
from django.db import models
from allauth.account.signals import user_logged_in, user_signed_up
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from direcciones.models import Localidad


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuario')
    telefono_fijo = models.CharField(max_length=11,verbose_name='telefono_fijo',blank=True)
    telefono_movil = models.CharField(max_length=11,verbose_name='telefono_móvil',blank=True)
    edad = models.CharField(max_length=2, verbose_name='edad',blank=True)
    fecha_nacimiento = models.DateField(blank=True,verbose_name='fecha de nacimiento',null=True)
    direccion = models.CharField(max_length=200, verbose_name='dirección',blank=True) 
    localidad = models.ForeignKey(Localidad, related_name='Localidades', verbose_name='Localidad',default=1)

    class Meta:
        verbose_name_plural='Perfiles de Usuario'

    def __str__(self):
        return '%s' % (self.user)

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

#HOMBRE = 'H' 
#MUJER = 'M'
#SEXO = ((HOMBRE,'Hombre'),
#        (MUJER,'Mujer'))
#sexo = models.CharField(max_length=1,default=1,verbose_name='sexo',choices=SEXO,blank=True)"""