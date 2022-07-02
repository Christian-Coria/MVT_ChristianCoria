from django.shortcuts import render
from mi_app.models import Parentezco, MisDatos


def presentando(request):
    context={}
    context["parientes"]= Parentezco.objects.all()

    return render(request,'mi_app/mis_parientes.html',context)

def presentandome(request):
    context={}
    context["datos_personales"]=MisDatos.objects.all()

    return render(request,'mi_app/mis_parientes.html',context)