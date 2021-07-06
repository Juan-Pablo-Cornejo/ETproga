from django.shortcuts import render, redirect
from .models import Colaborador
from .forms import ColaboradorForm

# Create your views here.

def home(request):
    colaboradores= Colaborador.objects.all()
    datos = {
        'colaboradores': colaboradores
    }
    return render(request, 'core/home.html', datos)
def crear_colab(request):
    if request.method == 'POST':
        colaborador_form = ColaboradorForm(request.POST)
        if colaborador_form.is_valid():
            colaborador_form.save()
            return redirect('home')
    else:
        colaborador_form = ColaboradorForm()
    return render(request, 'core/crear_colab.html', {'colaborador_form': colaborador_form})
def inicio(request):
    return render(request, 'core/inicio.html')
def modificar_colab(request):
    colaboradores= Colaborador.objects.all()
    return render(request, 'core/modificar_colab.html', {'colaboradores':colaboradores})
def modificar(request, id):
    colaboradores = Colaborador.objects.get(rutColaborador=id)
    datos ={
        'form': ColaboradorForm(instance=colaboradores)
    }
    if request.method == 'POST': 
        formulario = ColaboradorForm(data=request.POST, instance = colaboradores)
        if formulario.is_valid: 
            formulario.save()
            return redirect('home')
    return render(request, 'core/modificar_colab.html', datos)
def eliminar(request, id):
    colaboradores = Colaborador.objects.get( rutColaborador=id)
    colaboradores.delete()
    return redirect(to="home")