from contextvars import Context
from pipes import Template
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from numpy import product
from Apli.models import Family, VideoCards, VideoJuegos
from django.template import Template, Context
from django.conf.urls.static import static

from Apli.forms import Familyformulario,VideoCardsForms, VideoJuegosForm



# Son los archivos del entregable anterior.

def familiares(self):
    familiar1=Family(nombre='Leandro', apellido='Passalacqua', edad=41, fecha_de_nac='1980-11-23')
    familiar1.save()

    familiar2=Family(nombre='Sebastian', apellido='Passalacqua', edad=39, fecha_de_nac='1984-01-25')
    familiar2.save()

    familiar3=Family(nombre='Mauro', apellido='Passalacqua', edad=41, fecha_de_nac='1987-09-19')
    familiar3.save()

    documento=f'En la familia somos: {familiar1.nombre} ,  {familiar1.apellido}{ familiar1.edad } ,  {familiar1.fecha_de_nac}'

    return HttpResponse(documento)

def saludo(request):
        nombre= "Leandro"
        apellido= "Passalacqua"

        doc_externo= open("C:/PRUEBA/LEAN/Proyect/Templates/template1.html")
        
        plt=Template(doc_externo.read())

        doc_externo.close()

        ctx=Context({"nombre_persona": nombre,"apellido_persona": apellido})

        documento= plt.render(ctx)

        return HttpResponse(documento)

#Estos son los del segundo entregable


def inicio(request):

    return render(request, 'Apli/inicio.html')





def familia(request):

        form= Familyformulario()
        if request.method == 'POST':
            form = Familyformulario(request.POST)
            if form.is_valid():
                print('valido')
                product= Family()
                product.nombre=form.cleaned_data['nombre']
                product.apellido=form.cleaned_data['apellido']
                product.edad=form.cleaned_data['edad']
                product.fecha_de_nac=form.cleaned_data['fecha_de_nac']
                product.save()
                

            else:
                print('invalido')
        

        return render(request,'Apli/familia.html', {'form': form})



def placas(request):

        form=VideoCardsForms()
        if request.method == 'POST':
            form= VideoCardsForms(request.POST)
            if form.is_valid():
                print('valido')
                product=VideoCards()
                product.marca=form.cleaned_data['marca']
                product.modelo=form.cleaned_data['modelo']
                product.memoria=form.cleaned_data['memoria']
                product.save()
            else:
                print('invalido')

        return render(request, 'Apli/placas.html', {'form':form})



def videojuegos(request):
    form=VideoJuegosForm()
    if request.method == 'POST':
        form= VideoJuegosForm(request.POST)
        if form.is_valid():
            print('valido')
            product=VideoJuegos()
            product.nombre_del_juego=form.cleaned_data['nombre_del_juego']
            product.tipo_de_Juego=form.cleaned_data['tipo_de_Juego']
            product.espacio_en_disco=form.cleaned_data['espacio_en_disco']
            product.fecha_lanzamiento=form.cleaned_data['fecha_lanzamiento']
            product.save()
        else:
            print('invalido')

    
                

    return render(request, 'Apli/videojuegos.html', {'form': form})

# -----------------------------------------------------------------

    
def busqueda_quenobusca(request):
    
        return render(request,'Apli/buscar.html')
    
# 3---------------------------------------------------------------

def buscar(request):
    if request.GET['nombre']:
        variable_que_guarda_get=request.GET['nombre']
        variable_busca_filtra=Family.objects.filter(nombre__icontains=variable_que_guarda_get)
        

        return render(request,'Apli/buscar.html', {'nombre_diccionario': variable_busca_filtra, 'nombre':variable_que_guarda_get})

    else:
        respuesta="No enviaste datos correctos"

    return render(request, 'Apli/buscar.html', {'resp':respuesta})

# 1hasta aca------------------------------------------------------

# def buscar_familiar(request):
#     if request.GET["nombre"]:

#     lindo=request.GET["nombre"]

#     return render(request, 'Apli/buscar.html',{'jardin': lindo} )
    
            