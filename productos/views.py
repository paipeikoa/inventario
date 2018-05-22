# -*- coding: utf-8 -*-
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.list import ListView
from productos.forms import ProductoForm, ProveedorForm, CompraForm, DetalleCompraFormSet
from productos.models import Producto, Proveedor, Compra, DetalleCompra
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required,name='dispatch')
class ListadoProductos(ListView):
    model = Producto
    template_name = 'productos.html'
    context_object_name = 'productos'

@method_decorator(login_required,name='dispatch')
class ListadoProveedores(ListView):
    model = Proveedor
    template_name = 'proveedores.html'
    context_object_name = 'proveedores'

@method_decorator(login_required,name='dispatch')
class ListadoCompras(ListView):
    model = Compra
    template_name = 'compras.html'
    context_object_name = 'compras'

@method_decorator(login_required,name='dispatch')
class CrearProducto(CreateView):
    template_name = 'producto.html'
    form_class = ProductoForm
    success_url = reverse_lazy('productos:listado_productos')

@method_decorator(login_required,name='dispatch')
class CrearProveedor(CreateView):
    template_name = 'proveedor.html'
    form_class = ProveedorForm
    success_url = reverse_lazy('productos:listado_proveedores')

@method_decorator(login_required,name='dispatch')
class ModificarProducto(UpdateView):
    model = Producto
    template_name = 'producto.html'
    form_class = ProductoForm
    success_url = reverse_lazy('productos:listado_productos')

@method_decorator(login_required,name='dispatch')
class ModificarProveedor(UpdateView):
    model = Proveedor
    template_name = 'proveedor.html'
    form_class = ProveedorForm
    success_url = reverse_lazy('productos:listado_proveedores')

@method_decorator(login_required,name='dispatch')
class ModificarCompra(UpdateView):
    model = Compra
    template_name = 'compra.html'
    form_class = CompraForm
    success_url = reverse_lazy('productos:listado_compras')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detalles = DetalleCompra.objects.filter(compra=self.object).order_by('pk')
        detalles_data = []
        for detalle in detalles:
            d = {'producto': detalle.producto,
                 'cantidad': detalle.cantidad,
                 'precio_compra': detalle.producto.precio}
            detalles_data.append(d)
        detalle_compra_form_set = DetalleCompraFormSet(initial=detalles_data)
        return self.render_to_response(self.get_context_data(form=form,
                                                             detalle_compra_form_set=detalle_compra_form_set))


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detalle_compra_form_set = DetalleCompraFormSet(request.POST)
        if form.is_valid() and detalle_compra_form_set.is_valid():
            return self.form_valid(form, detalle_compra_form_set)
        else:
            return self.form_invalid(form, detalle_compra_form_set)


    def form_valid(self, form, detalle_compra_form_set):
        self.object = form.save()
        detalle_compra_form_set.instance = self.object
        DetalleCompra.objects.filter(compra = self.object).delete()
        detalle_compra_form_set.save()
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form, detalle_compra_form_set):
        return self.render_to_response(self.get_context_data(form=form,
                                                             detalle_compra_form_set = detalle_compra_form_set))

@method_decorator(login_required,name='dispatch')
class DetalleProducto(DetailView):
    model = Producto
    template_name = 'detalle_producto.html'

@method_decorator(login_required,name='dispatch')
class DetalleProveedor(DetailView):
    model = Proveedor
    template_name = 'detalle_proveedor.html'

@method_decorator(login_required,name='dispatch')
class DetalleCompras(DetailView):
    model = DetalleCompra
    template_name = 'detalle_compra.html'


@method_decorator(login_required,name='dispatch')
class CrearCompra(CreateView):
    model = Compra
    template_name = 'compra.html'
    form_class = CompraForm
    success_url = reverse_lazy('productos:listado_compras')

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detalle_orden_compra_formset=DetalleCompraFormSet()
        return self.render_to_response(self.get_context_data(form=form,
                                                             detalle_compra_form_set=detalle_orden_compra_formset))

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detalle_compra_form_set = DetalleCompraFormSet(request.POST)
        if form.is_valid() and detalle_compra_form_set.is_valid():
            return self.form_valid(form, detalle_compra_form_set)
        else:
            return self.form_invalid(form, detalle_compra_form_set)


    def form_valid(self, form, detalle_compra_form_set):
        self.object = form.save()
        detalle_compra_form_set.instance = self.object
        detalle_compra_form_set.save()
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form, detalle_compra_form_set):
        return self.render_to_response(self.get_context_data(form=form,
                                                             detalle_compra_form_set = detalle_compra_form_set))
