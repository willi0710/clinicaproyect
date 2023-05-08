from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import cita
from .forms import citaForm


# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')
def especialistas(request):
    return render(request, 'paginas/especialistas.html')

def citas(request):
    citas = cita.objects.all()
    return render(request, 'citas/index.html', {'citas': citas})

def solicitarGnral(request):
    formulario = citaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('citas')
    return render(request, 'citas/solicitarGnral.html', {'formulario': formulario})

def modificar(request, id):
    citax = cita.objects.get(id=id)
    formulario = citaForm(request.POST or None, request.FILES or None, instance=citax)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('citas')
    return render(request, 'citas/modificar.html', {'formulario': formulario})

def eliminar(request, id):
        citax = cita.objects.get(id=id)
        citax.delete()
        return redirect('citas')