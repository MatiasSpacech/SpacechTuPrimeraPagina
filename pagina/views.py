from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def pagina(request):
    return render(request , 'principal.html')