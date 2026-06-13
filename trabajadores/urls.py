from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_trabajadores, name='lista_trabajadores'),
    path('crear/', views.crear_trabajador, name='crear_trabajador'),
    path('editar/<int:pk>/', views.editar_trabajador, name='editar_trabajador'),
    path('eliminar/<int:pk>/', views.eliminar_trabajador, name='eliminar_trabajador'),  

    path('json/<int:pk>/', views.trabajador_json, name='trabajador_json'),
]