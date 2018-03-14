# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.mail import send_mail

from django.conf import settings
from .forms import contactForm

def contact(request):
    title = 'Contact'
    form = contactForm(request.POST or None)
    confirm_message = None
    if form.is_valid():
        name = form.cleaned_data['name']
        message = form.cleaned_data['message']
        subject = 'Enlacerv'
        emailFrom = form.cleaned_data['email']
        message = '%s \n\n%s \n\n%s' %(name,emailFrom,message,)
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject,message,emailFrom,emailTo,fail_silently=True)
        title = "¡Muchas Gracias!"
        confirm_message = "A la brevedad nos pondremos en contacto con usted."
        form = None

    context = {'title': title,'form':form,  'confirm_message':confirm_message}
    templates = 'contact.html'
    return render(request,templates,context)