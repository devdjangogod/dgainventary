from django.shortcuts import render, redirect, get_object_or_404
from .models import Trabajador
from .forms import TrabajadorForm

def lista_trabajadores(request):
    trabajadores = Trabajador.objects.all().order_by('-id')
    return render(request, 'trabajadores/lista.html', {
        'trabajadores': trabajadores
    })

def crear_trabajador(request):
    form = TrabajadorForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('lista_trabajadores')

    return render(request, 'trabajadores/form.html', {
        'form': form,
        'titulo': 'Nuevo trabajador'
    })

def editar_trabajador(request, pk):
    trabajador = get_object_or_404(Trabajador, pk=pk)
    form = TrabajadorForm(request.POST or None, instance=trabajador)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('lista_trabajadores')

    return render(request, 'trabajadores/form.html', {
        'form': form,
        'titulo': 'Editar trabajador'
    })

def eliminar_trabajador(request, pk):
    trabajador = get_object_or_404(Trabajador, pk=pk)
    trabajador.delete()
    return redirect('lista_trabajadores')


from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Trabajador


def trabajador_json(request, pk):
    trabajador = get_object_or_404(Trabajador, pk=pk)

    return JsonResponse({
        'usuario': trabajador.usuario,
        'dni': trabajador.dni,
        'sede': trabajador.sede,
        'local': trabajador.local,
        'dependencia': trabajador.dependencia,
        'unidad': trabajador.unidad,
        'area': trabajador.area,
        'sub_area': trabajador.sub_area,
        'ambiente': trabajador.ambiente,
        'piso': trabajador.piso,
        'referencia': trabajador.referencia,
    })  