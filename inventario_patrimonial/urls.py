from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("inventario/", views.registros_inventario, name="registros_inventario"),
    path("inventario/crear/", views.crear_bien, name="crear_bien"),
    path("inventario/editar/<int:pk>/", views.editar_bien, name="editar_bien"),
    path("inventario/eliminar/<int:pk>/", views.eliminar_bien, name="eliminar_bien"),
    path("reportes/", views.reportes, name="reportes"),
    path("configuracion/", views.configuracion, name="configuracion"),

    # urls.py
    path('ficha/<int:pk>/', views.ficha_inventario, name='ficha_inventario'),

]