from django.shortcuts import render , redirect
from django.http import HttpResponse
from pagina.models import Auto
from pagina.forms import formularioAutos
# Create your views here.
def pagina(request):
    return render(request , 'principal.html')

def lista_de_autos(request):
    autos= Auto.objects.all()
    return render(request, 'autos.html', {'autos': autos})
    
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
        
    return render(request, 'agregar-autos.html', {'formulario': formulario})
    
 