from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import BienInventario
from .forms import BienInventarioForm


def dashboard(request):
    return render(request, "inventario_patrimonial/dashboard.html")


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

    # return render(request, "inventario_patrimonial/formulario.html", {
    #     "form": form,
    #     "titulo": "Nuevo registro de inventario"
    # })

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

    # return render(request, "inventario_patrimonial/formulario.html", {
    #     "form": form,
    #     "titulo": "Editar registro de inventario"
    # })

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




