from django import forms

class formularioAutos (forms.Form):
    marca = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=20)
    color = forms.CharField(max_length=20)
    kilometros = forms.IntegerField()