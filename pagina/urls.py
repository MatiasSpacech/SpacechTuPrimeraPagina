from django.urls import path
from pagina.views import pagina

urlpatterns = [
    path('', pagina, name = 'principal'),

]