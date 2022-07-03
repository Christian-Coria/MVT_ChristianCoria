from django.shortcuts import render
from mi_app.models import Parentezco,MisMascotas,MisDatos


def presentando(request):
    context={}
    context["parientes"]= Parentezco.objects.all()

    return render(request,'mi_app/mis_parientes.html',context)

def presentandome(request):
    context={}
    context["mis_datos"] =MisDatos.objects.all()    

    return render(request,'mi_app/mis_datos.html',context)


def presentando_mascotas(request):
    context={}
    context["mascotas"]=MisMascotas.objects.all()

    return render(request,'mi_app/mis_mascotas.html',context)