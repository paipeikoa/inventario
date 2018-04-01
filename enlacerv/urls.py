"""enlacerv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from usuarios import views as usuarios_views
from contact import views as contact_views
from direcciones import views as direcciones_views
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', usuarios_views.home, name='home'),
    url(r'^about/$', usuarios_views.about, name='about'),
    url(r'^contact/$', contact_views.contact, name='contact'),
    url(r'^profile/$', usuarios_views.view_profile, name='profile'),
    url(r'^edit-profile/$', usuarios_views.edit_profile, name='edit-profile'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^avatar/', include('avatar.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)