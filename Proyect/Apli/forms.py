from django import forms

class Familyformulario(forms.Form):
    nombre= forms.CharField(label='Nombre', max_length=30)
    apellido= forms.CharField(label='Apellido', max_length=30)
    edad= forms.IntegerField()
    fecha_de_nac= forms.DateField()

class VideoCardsForms(forms.Form):
    marca= forms.CharField(max_length=30)
    modelo=forms.CharField(max_length=30)
    memoria=forms.IntegerField()


class VideoJuegosForm(forms.Form):
    nombre_del_juego=forms.CharField(max_length=10)
    tipo_de_Juego= forms.CharField(max_length=10)
    espacio_en_disco=forms.IntegerField()
    fecha_lanzamiento=forms.DateField()