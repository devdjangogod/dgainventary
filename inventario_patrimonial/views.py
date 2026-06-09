from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import BienInventario
from .forms import BienInventarioForm

from django.shortcuts import render
from .models import BienInventario

from django.db.models import Count
from .models import BienInventario

import json
from django.db.models import Count
from .models import BienInventario

def dashboard(request):
    total_bienes = BienInventario.objects.count()
    total_usuarios = BienInventario.objects.values('usuario_responsable').distinct().count()
    total_ambientes = BienInventario.objects.values('nombre_ambiente').distinct().count()
    total_sedes = BienInventario.objects.values('sede_filial').distinct().count()

    bienes_por_sede = BienInventario.objects.values('sede_filial').annotate(
        total=Count('id')
    ).order_by('-total')[:5]

    bienes_por_dependencia = BienInventario.objects.values('dependencia').annotate(
        total=Count('id')
    ).order_by('-total')[:5]

    bienes_por_marca = BienInventario.objects.values('marca').annotate(
        total=Count('id')
    ).order_by('-total')[:5]

    ultimos_bienes = BienInventario.objects.all().order_by('-id')[:8]

    return render(request, 'inventario_patrimonial/dashboard.html', {
        'total_bienes': total_bienes,
        'total_usuarios': total_usuarios,
        'total_ambientes': total_ambientes,
        'total_sedes': total_sedes,

        'bienes_por_sede': bienes_por_sede,
        'bienes_por_dependencia': bienes_por_dependencia,
        'bienes_por_marca': bienes_por_marca,
        'ultimos_bienes': ultimos_bienes,

        'sedes_labels': json.dumps([x['sede_filial'] or 'Sin sede' for x in bienes_por_sede]),
        'sedes_data': json.dumps([x['total'] for x in bienes_por_sede]),

        'marcas_labels': json.dumps([x['marca'] or 'Sin marca' for x in bienes_por_marca]),
        'marcas_data': json.dumps([x['total'] for x in bienes_por_marca]),
    })

def registros_inventario(request):
    bienes = BienInventario.objects.all().order_by("-creado")

    q = request.GET.get("q")
    if q:
        bienes = bienes.filter(
            Q(descripcion__icontains=q) |
            Q(cod_inv_2025__icontains=q) |
            Q(codigo_patrimonial_conciliado__icontains=q) |
            Q(usuario_responsable__icontains=q) |
            Q(nombre_ambiente__icontains=q)
        )

    return render(request, "inventario_patrimonial/registros.html", {
        "bienes": bienes
    })


def crear_bien(request):
    if request.method == "POST":
        form = BienInventarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("registros_inventario")
    else:
        form = BienInventarioForm()

    return render(request, 'inventario_patrimonial/formulario.html', {
        'form': form,
        'titulo': 'Nuevo Registro',
        'modo_edicion': False,
    })




def editar_bien(request, pk):
    bien = get_object_or_404(BienInventario, pk=pk)

    if request.method == "POST":
        form = BienInventarioForm(request.POST, instance=bien)
        if form.is_valid():
            form.save()
            return redirect("registros_inventario")
    else:
        form = BienInventarioForm(instance=bien)

    return render(request, 'inventario_patrimonial/formulario.html', {
        'form': form,
        'titulo': 'Editar Registro',
        'modo_edicion': True,
    })




def eliminar_bien(request, pk):
    bien = get_object_or_404(BienInventario, pk=pk)
    bien.delete()
    return redirect("registros_inventario")


def reportes(request):
    return render(request, "inventario_patrimonial/reportes.html")


def configuracion(request):
    return render(request, "inventario_patrimonial/configuracion.html")




# views.py
from django.shortcuts import render, get_object_or_404
from .models import BienInventario

def ficha_inventario(request, pk):
    bien = get_object_or_404(BienInventario, pk=pk)

    bienes = BienInventario.objects.filter(
        usuario_responsable=bien.usuario_responsable,
        dni=bien.dni,
        sede_filial=bien.sede_filial,
        local=bien.local,
        dependencia=bien.dependencia,
        unidad_nivel_1=bien.unidad_nivel_1,
        area_nivel_2=bien.area_nivel_2,
        sub_area_nivel_3=bien.sub_area_nivel_3,
        nombre_ambiente=bien.nombre_ambiente,
        piso_nivel=bien.piso_nivel,
        referencia_ubicacion=bien.referencia_ubicacion,
    ).order_by('id')

    return render(request, 'inventario_patrimonial/ficha_inventario.html', {
        'bien': bien,
        'bienes': bienes,
    })




