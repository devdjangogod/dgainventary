from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", include("inventario_patrimonial.urls")),
    path('usuarios/', include('usuarios.urls')),
    path('trabajadores/', include('trabajadores.urls')),    
]