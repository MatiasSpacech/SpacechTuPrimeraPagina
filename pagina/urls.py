from django.urls import path
from pagina.views import pagina, agregar_autos ,lista_de_autos, ver_auto, eliminar_auto, editar_auto

urlpatterns = [
    path('', pagina, name = 'principal'),
    path('autos/nuevo', agregar_autos, name = 'AgregarAutos'),
    path('autos', lista_de_autos, name = 'Autos'), 
    path('autos/<int:id_auto>' , ver_auto, name = 'ver_auto' ),
    path('autos/<int:id_auto>/eliminar' , eliminar_auto, name = 'eliminar_auto' ),
    path('autos/<int:id_auto>/editar' , editar_auto, name = 'editar_auto' )       
]
