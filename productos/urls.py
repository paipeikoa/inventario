from django.conf.urls import url
from productos.views import (
                            HomeInventario,
                            ListadoProductos,
                            CrearProducto,
                            ModificarProducto,
                            DetalleProducto,
                            EliminarProducto,
                            ListadoCategorias,
                            CrearCategoria,
                            ModificarCategoria,
                            DetalleCategoria,
                            EliminarCategoria)

urlpatterns = [
    url(r'^$', HomeInventario.as_view(), name="home_inventario"),
    url(r'^listado_productos/$', ListadoProductos.as_view(), name="listado_productos"),
    url(r'^crear_producto/$', CrearProducto.as_view(), name="crear_producto"),
    url(r'^modificar_producto/(?P<pk>.+)/$',ModificarProducto.as_view(), name="modificar_producto"),
    url(r'^detalle_producto/(?P<pk>.+)/$',DetalleProducto.as_view(), name="detalle_producto"),
    url(r'^eliminar_producto/(?P<pk>.+)/$',EliminarProducto.as_view(), name="eliminar_producto"),
    url(r'^listado_categorias$', ListadoCategorias.as_view(), name="listado_categorias"),
    url(r'^crear_categoria/$', CrearCategoria.as_view(), name="crear_categoria"),
    url(r'^modificar_categoria/(?P<pk>.+)/$',ModificarCategoria.as_view(), name="modificar_categoria"),
    url(r'^detalle_categoria/(?P<pk>.+)/$',DetalleCategoria.as_view(), name="detalle_categoria"),
    url(r'^eliminar_categoria/(?P<pk>.+)/$',EliminarCategoria.as_view(), name="eliminar_categoria"),
]

