from django import forms

class formsHuron(forms.Form):
    nombre=forms.CharField(max_length=30)
    edad=forms.IntegerField()
    raza=forms.CharField(max_length=30)

class formsComida(forms.Form):
    tipo=forms.CharField(max_length=30)
    proteinas=forms.IntegerField()

class formsAccessory(forms.Form):
    tipo=forms.CharField(max_length=30)
    precio=forms.IntegerField()
    color=forms.CharField(max_length=30)