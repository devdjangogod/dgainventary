from django.urls import path
from . import views

urlpatterns = [
    path('myadmin/', views.dashboard, name='dashboard'),
    path('myadmin/nuevo/', views.crear_documento, name='crear_documento'),
    path('myadmin/salida/<int:pk>/', views.registrar_salida, name='registrar_salida'),
    path('myadmin/editar/<int:pk>/', views.editar_documento, name='editar_documento'),
    path('myadmin/eliminar/<int:pk>/', views.eliminar_documento, name='eliminar_documento'),

    path(
    'myadmin/archivar/<int:pk>/',
    views.archivar_documento,
    name='archivar_documento'
),

path('myadmin/detalle/<int:pk>/', views.detalle_documento, name='detalle_documento'),
]