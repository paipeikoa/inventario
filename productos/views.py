# -*- coding: utf-8 -*-
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from productos.models import Producto, Categoria
from productos.forms import ProductoForm, CategoriaForm
from usuarios.models import UserProfile


@method_decorator(login_required, name='dispatch')
class HomeInventario(ListView):
    model = Producto
    template_name = 'inventario.html'

    def get_context_data(self, **kwargs):
        productos = Producto.objects.all().count()
        categorias = Categoria.objects.all().count()
        usuarios = UserProfile.objects.all().count()
        context = super(HomeInventario, self).get_context_data(**kwargs)
        context.update({'produ': productos, 'categ': categorias, 'usuarios': usuarios})
        return context


@method_decorator(login_required, name='dispatch')
class ListadoProductos(ListView):
    model = Producto
    template_name = 'productos.html'
    context_object_name = 'productos'


@method_decorator(login_required, name='dispatch')
class CrearProducto(CreateView):
    template_name = 'producto.html'
    form_class = ProductoForm
    success_url = reverse_lazy('productos:listado_productos')


@method_decorator(login_required, name='dispatch')
class ModificarProducto(UpdateView):
    model = Producto
    template_name = 'producto.html'
    form_class = ProductoForm
    success_url = reverse_lazy('productos:listado_productos')


@method_decorator(login_required, name='dispatch')
class DetalleProducto(DetailView):
    model = Producto
    template_name = 'detalle_producto.html'


@method_decorator(login_required, name='dispatch')
class EliminarProducto(DeleteView):
    model = Producto
    success_url = reverse_lazy('productos:listado_productos')


# --------------  Categorias  --------------------- #
 

@method_decorator(login_required, name='dispatch')
class ListadoCategorias(ListView):
    model = Categoria
    template_name = 'categorias.html'
    context_object_name = 'categorias'


@method_decorator(login_required, name='dispatch')
class CrearCategoria(CreateView):
    template_name = 'categoria.html'
    form_class = CategoriaForm
    success_url = reverse_lazy('productos:listado_categorias')


@method_decorator(login_required, name='dispatch')
class ModificarCategoria(UpdateView):
    model = Categoria
    template_name = 'categoria.html'
    form_class = CategoriaForm
    success_url = reverse_lazy('productos:listado_categorias')


@method_decorator(login_required, name='dispatch')
class DetalleCategoria(DetailView):
    model = Categoria
    template_name = 'detalle_categoria.html'


@method_decorator(login_required, name='dispatch')
class EliminarCategoria(DeleteView):
    model = Categoria
    success_url = reverse_lazy('productos:listado_categorias')
