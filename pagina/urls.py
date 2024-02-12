from django.urls import path
from pagina.views import pagina, agregar_autos ,lista_de_autos

urlpatterns = [
    path('', pagina, name = 'principal'),
    path('autos/nuevo', agregar_autos, name = 'AgregarAutos'),
    path('autos', lista_de_autos, name = 'Autos')        
]
