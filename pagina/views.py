from django.shortcuts import render , redirect
from django.http import HttpResponse
from pagina.models import Auto
from pagina.forms import formularioAutos, BuscarAuto, formularioEdicionAutos
# Create your views here.
def pagina(request):
    return render(request , 'pagina/principal.html')
    #return render(request , 'base.html')

def lista_de_autos(request):
    formulario = BuscarAuto(request.GET)
    if formulario.is_valid():
        modelo_a_buscar = formulario.cleaned_data.get('modelo')
        autos = Auto.objects.filter(modelo__icontains=modelo_a_buscar)
    return render(request, 'pagina/autos.html', {'autos': autos , 'formulario': formulario})
    
def agregar_autos (request):
    formulario = formularioAutos()
    if request.method == "POST":
        formulario = formularioAutos(request.POST)
        if formulario.is_valid():
            marca = formulario.cleaned_data.get('marca')
            modelo = formulario.cleaned_data.get('modelo')
            color = formulario.cleaned_data.get('color')
            kilometros = formulario.cleaned_data.get('kilometros')
            
            auto = Auto(marca=marca, modelo=modelo, color=color, kilometros=kilometros)
            auto.save()
            return redirect("Autos")
        
    return render(request, 'pagina/agregar-autos.html', {'formulario': formulario})
    
def ver_auto(request, id_auto):
    auto = Auto.objects.get(id=id_auto)
    return render(request, 'pagina/ver_auto.html', {'auto':auto})

def eliminar_auto(request, id_auto):
    auto = Auto.objects.get(id=id_auto)
    auto.delete()
    return redirect('Autos')

def editar_auto(request, id_auto):
    auto = Auto.objects.get(id=id_auto)
    formulario = formularioEdicionAutos(initial={'marca': auto.marca , 'modelo': auto.modelo , 'color': auto.color, 'kilometros': auto.kilometros})
    if request.method == "POST":
        formulario = formularioEdicionAutos(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            auto.marca = info.get('marca')
            auto.modelo = info.get('modelo')
            auto.color = info.get('color')
            auto.kilometros = info.get('kilometros')
            auto.save()
            return redirect('Autos')
    return render(request, 'pagina/editar_auto.html' , {'auto': auto , 'formulario': formulario})