from django.urls import path
from . import views

urlpatterns = [
    path('myadmin/', views.dashboard, name='dashboard'),
    path('myadmin/nuevo/', views.crear_documento, name='crear_documento'),
    path('myadmin/salida/<int:pk>/', views.registrar_salida, name='registrar_salida'),
    path('myadmin/editar/<int:pk>/', views.editar_documento, name='editar_documento'),
    path('myadmin/eliminar/<int:pk>/', views.eliminar_documento, name='eliminar_documento'),
    path('myadmin/archivar/<int:pk>/', views.archivar_documento, name='archivar_documento'),
    path('myadmin/detalle/<int:pk>/', views.detalle_documento, name='detalle_documento'),

    path('verificar-documento/', views.verificar_documento, name='verificar_documento'),

    path('obtener-numero-documento/', views.obtener_numero_documento, name='obtener_numero_documento'),

    path('registros-documentos/', views.registros_documentos, name='registros_documentos'),


    path('registros/', views.registros_documentos, name='registros_documentos'),
    path('reportes/', views.reportes, name='reportes'),
    path('configuracion/', views.configuracion, name='configuracion'),

    path(
        'reservar-numero-documento/',
        views.reserva_numero_documento,
        name='reserva_numero_documento'
    ),

    path(
        'reservas-documentos/',
        views.reservas_documentos,
        name='reservas_documentos'
    ),



path(
    'guardar-reserva-ajax/',
    views.guardar_reserva_ajax,
    name='guardar_reserva_ajax'
),


]