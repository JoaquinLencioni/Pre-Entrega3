from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
from app_coder.forms import pasajeroformulario,hotelesformulario, viajesformulario
from app_coder.models import Pasajero,Hoteles,viajes
from django.http import HttpResponse
from datetime import datetime


def inicio(request):
    return render(request, "app_coder/inicio.html")


#Formularios
def formulario1(request):
    if request.method == "POST":
        miformulario=pasajeroformulario(request.POST)
        print(miformulario)
      
        if miformulario.is_valid:
            informacion1=miformulario.cleaned_data
            newPasajero =Pasajero(str(informacion1["Nombre"]),
                     str(informacion1["Apellido"]),
                     str(informacion1["Identificación"]),
                     str(informacion1["Email"]),
                     (informacion1["Fecha_de_nacimiento"]))
            newPasajero.save()
            return render(request, "app_coder/inicio.html")
    else:
        miformulario = pasajeroformulario()
    return render(request, "app_coder/pasajeroformulario.html",{"miformulario":miformulario})
    
    
def formulario2(request):
    if request.method == "POST":
        miformulario2=hotelesformulario(request.POST)
        print(miformulario2)
      
        if miformulario2.is_valid:
            informacion2=miformulario2.cleaned_data
            newhotel = Hoteles(str(informacion2["Codigo_de_reserva"]),str(informacion2["Nombre_del_hotel"]), 
                              str(informacion2["Dirección"]),
                              str(informacion2["Identificación_del_pasajero"]),
                              str(informacion2["Ciudad"]),
                              str(informacion2["Fecha_de_ingreso"]),
                              int(informacion2["Cantidad_de_noches"]),
                              str(informacion2["Contacto_email"]))
            newhotel.save()
            return render(request,"app_coder/inicio.html")
    else:
        miformulario2 = hotelesformulario()
    return render(request, "app_coder/hotelesformulario.html",{"miformulario2":miformulario2})



def formulario3(request):
    if request.method == "POST":
        miformulario3=viajesformulario(request.POST)
        print(miformulario3)
      
        if miformulario3.is_valid:
            informacion3=miformulario3.cleaned_data
            newviaje = viajes(str(informacion3["Codigo_de_reserva"]),str(informacion3["Origen"]),str(informacion3["Destino"]),
                              (informacion3["Fecha_de_partida"]),str(informacion3["Pasajero_ID"]),int(informacion3["Cantidad_de_pasajeros"]),
                              str(informacion3["Comentarios"]))
            newviaje.save()
            return render(request,"app_coder/inicio.html")
    else:
        miformulario3 = viajesformulario()
    return render(request, "app_coder/viajesformulario.html",{"miformulario3":miformulario3})



def busqueda_pasajero(request):
     return render(request,'app_coder/busqueda_pasajero.html')  
 

def buscar(request):
    if request.GET['id_buscado']: 
        id_pasajero = request.GET['id_buscado']
        resultado= Pasajero.objects.filter(pasajero_id__icontains=id_pasajero)
        resultado_viajes=viajes.objects.filter(viajes_pasajero_id__icontains=id_pasajero)
        return render(request,'app_coder/resultado_busqueda_pasajero.html', {"resultado":resultado, "resultado_viajes":resultado_viajes})
    else:
        respuesta= "No encontrado"
        return HttpResponse(respuesta)
