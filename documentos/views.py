from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Documento
from .forms import EntradaDocumentoForm, SalidaDocumentoForm

from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.http import JsonResponse
from .models import Documento

from .forms import DocumentoForm

from django.http import JsonResponse
from .models import Documento

from django.shortcuts import render
from .models import Documento

import json
from django.views.decorators.http import require_POST
from django.db import IntegrityError




def dashboard(request):
    documentos = Documento.objects.all().order_by('-creado')
    return render(request, 'documentos/dashboard.html', {
        'documentos': documentos
    })


from .models import ReservaDocumento

def crear_documento(request):

    if request.method == 'POST':
        form = DocumentoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('registros_documentos')

        print(form.errors)

    else:
        form = DocumentoForm()

    reservas = ReservaDocumento.objects.all().order_by('-fecha_reserva')

    return render(request, 'documentos/formulario_entrada.html', {
        'form': form,
        'reservas': reservas,
        'titulo': 'Registrar Documento'
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





def verificar_documento(request):
    expediente = request.GET.get('expediente', '')
    registro = request.GET.get('registro', '')
    adjunto = request.GET.get('adjunto', '')

    return JsonResponse({
        'expediente_existe': Documento.objects.filter(
            numero_expediente=expediente
        ).exists(),

        'registro_existe': Documento.objects.filter(
            numero_registro_principal=registro
        ).exists(),

        'adjunto_existe_como_expediente': Documento.objects.filter(
            numero_expediente=adjunto
        ).exists(),
    })



def obtener_numero_documento(request):
    tipo = request.GET.get('tipo')

    ultimo = Documento.objects.filter(
        tipo_documento=tipo
    ).order_by('-id').first()

    if ultimo and ultimo.numero_documento.isdigit():
        siguiente = int(ultimo.numero_documento) + 1
    else:
        siguiente = 1

    return JsonResponse({
        'numero': str(siguiente).zfill(3)
    })



def registros_documentos(request):
    documentos = Documento.objects.all().order_by('-fecha_ingreso')

    return render(
        request,
        'documentos/registros_documentos.html',
        {'documentos': documentos}
    )





def configuracion(request):
    return render(request, 'documentos/configuracion.html')





def reportes(request):

    tipo = request.GET.get('tipo', 'OFICIO')

    documentos = Documento.objects.filter(
        tipo_documento=tipo
    )

    registrados = {}

    for doc in documentos:
        registrados[doc.numero_documento] = {
            "autor": doc.autor,
            "estado": doc.estado
        }

    numeros = []
    contador = 1

    for fila in range(25):
        columnas = []

        for col in range(12):
            numero = str(contador).zfill(3)

            columnas.append({
                "numero": numero,
                "registrado": numero in registrados,
                "autor": registrados.get(numero, {}).get("autor", ""),
                "estado": registrados.get(numero, {}).get("estado", ""),
            })

            contador += 1

        numeros.append(columnas)

    return render(
        request,
        "documentos/reportes.html",
        {
            "numeros": numeros,
            "tipo_actual": tipo,
            "tipos": Documento.TIPO_DOCUMENTO,
        }
    )



from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ReservaDocumento
from .forms import ReservaDocumentoForm

def reserva_numero_documento(request):
    tipo_actual = request.GET.get('tipo', '')

    numeros = []

    if tipo_actual:
        documentos = Documento.objects.filter(
            tipo_documento=tipo_actual
        ).values('numero_documento', 'autor')

        reservas = ReservaDocumento.objects.filter(
            tipo_documento=tipo_actual
        ).values('numero_documento', 'autor')

        ocupados = {}

        for doc in documentos:
            ocupados[doc['numero_documento']] = {
                'autor': doc['autor'],
                'origen': 'DOCUMENTO'
            }

        for reserva in reservas:
            ocupados[reserva['numero_documento']] = {
                'autor': reserva['autor'],
                'origen': 'RESERVA'
            }

        lista = []

        for i in range(1, 301):
            numero = str(i).zfill(3)

            if numero in ocupados:
                lista.append({
                    'numero': numero,
                    'reservado': True,
                    'autor': ocupados[numero]['autor'],
                    'origen': ocupados[numero]['origen'],
                })
            else:
                lista.append({
                    'numero': numero,
                    'reservado': False,
                    'autor': '',
                    'origen': '',
                })

        numeros = [
            lista[i:i + 12]
            for i in range(0, len(lista), 12)
        ]

    return render(request, 'documentos/reserva_numero_documento.html', {
        'tipos': Documento.TIPO_DOCUMENTO,
        'autores': Documento.AUTORES,
        'tipo_actual': tipo_actual,
        'numeros': numeros,
    })




def reservas_documentos(request):

    reservas = ReservaDocumento.objects.all().order_by(
        '-fecha_reserva'
    )

    return render(
        request,
        'documentos/reservas_documentos.html',
        {
            'reservas': reservas
        }
    )



import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import ReservaDocumento, Documento


@require_POST
def guardar_reserva_ajax(request):
    try:
        data = json.loads(request.body)

        tipo_documento = data.get('tipo_documento')
        numero_documento = data.get('numero_documento')
        autor = data.get('autor')

        if not tipo_documento or not numero_documento or not autor:
            return JsonResponse({
                'ok': False,
                'error': 'Datos incompletos.'
            })

        existe_documento = Documento.objects.filter(
            tipo_documento=tipo_documento,
            numero_documento=numero_documento
        ).exists()

        if existe_documento:
            return JsonResponse({
                'ok': False,
                'error': 'Este número ya pertenece a un documento registrado.'
            })

        reserva, created = ReservaDocumento.objects.update_or_create(
            tipo_documento=tipo_documento,
            numero_documento=numero_documento,
            defaults={
                'autor': autor
            }
        )

        return JsonResponse({
            'ok': True,
            'autor': reserva.autor,
            'created': created
        })

    except Exception as e:
        return JsonResponse({
            'ok': False,
            'error': str(e)
        })