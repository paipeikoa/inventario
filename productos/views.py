# -*- coding: utf-8 -*-
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from productos.forms import ProductoForm, CategoriaForm
from productos.models import Producto, Categoria
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required,name='dispatch')
class ListadoProductos(ListView):
    model = Producto
    template_name = 'productos.html'
    context_object_name = 'productos'


@method_decorator(login_required,name='dispatch')
class CrearProducto(CreateView):
    template_name = 'producto.html'
    form_class = ProductoForm
    success_url = reverse_lazy('productos:listado_productos')


@method_decorator(login_required,name='dispatch')
class ModificarProducto(UpdateView):
    model = Producto
    template_name = 'producto.html'
    form_class = ProductoForm
    success_url = reverse_lazy('productos:listado_productos')


@method_decorator(login_required,name='dispatch')
class DetalleProducto(DetailView):
    model = Producto
    template_name = 'detalle_producto.html'


@method_decorator(login_required,name='dispatch')
class EliminarProducto(DeleteView):
    model = Producto
    success_url = reverse_lazy('productos:listado_productos')
