from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Documento
from .forms import EntradaDocumentoForm, SalidaDocumentoForm

from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)




def dashboard(request):
    documentos = Documento.objects.all().order_by('-creado')
    return render(request, 'documentos/dashboard.html', {
        'documentos': documentos
    })


def crear_documento(request):
    if request.method == 'POST':
        form = EntradaDocumentoForm(request.POST)
        if form.is_valid():
            documento = form.save(commit=False)
            documento.fecha_ingreso = timezone.now().date()
            documento.save()
            return redirect('dashboard')
    else:
        form = EntradaDocumentoForm()

    return render(request, 'documentos/formulario_entrada.html', {
        'form': form,
        'titulo': 'Registro de entrada'
    })


def registrar_salida(request, pk):

    documento = get_object_or_404(
        Documento,
        pk=pk
    )

    # Ya archivado
    if documento.estado == 'ARCHIVADO':
        return redirect(
            'detalle_documento',
            pk=documento.id
        )

    # Ya tiene salida registrada
    if documento.estado == 'DERIVADO':
        return redirect(
            'detalle_documento',
            pk=documento.id
        )

    if request.method == 'POST':

        form = SalidaDocumentoForm(
            request.POST,
            instance=documento
        )

        if form.is_valid():

            documento = form.save(
                commit=False
            )

            documento.estado = 'DERIVADO'

            documento.save()

            return redirect(
                'detalle_documento',
                pk=documento.id
            )

    else:

        form = SalidaDocumentoForm(
            instance=documento
        )

    return render(
        request,
        'documentos/formulario_salida.html',
        {
            'form': form,
            'documento': documento,
            'titulo': 'Registro de salida'
        }
    )


def editar_documento(request, pk):

    documento = get_object_or_404(
        Documento,
        pk=pk
    )

    # Si está archivado no permitir edición
    if documento.estado == 'ARCHIVADO':
        return redirect('detalle_documento', pk=documento.id)

    if request.method == 'POST':

        form = EntradaDocumentoForm(
            request.POST,
            instance=documento
        )

        if form.is_valid():
            form.save()

            return redirect(
                'detalle_documento',
                pk=documento.id
            )

    else:

        form = EntradaDocumentoForm(
            instance=documento
        )

    return render(
        request,
        'documentos/formulario_entrada.html',
        {
            'form': form,
            'titulo': 'Editar registro de entrada',
            'documento': documento
        }
    )


def eliminar_documento(request, pk):
    documento = get_object_or_404(Documento, pk=pk)
    documento.delete()
    return redirect('dashboard')


def archivar_documento(request, pk):
    documento = get_object_or_404(
        Documento,
        pk=pk
    )

    documento.estado = 'ARCHIVADO'
    documento.save()

    return redirect('dashboard')



def detalle_documento(request, pk):
    documento = get_object_or_404(Documento, pk=pk)

    return render(request, 'documentos/detalle_documento.html', {
        'documento': documento
    })