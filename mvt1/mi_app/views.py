from django.shortcuts import render
from mi_app.models import Parentezco


def presentando(request):
    context={}
    context["parientes"]= Parentezco.objects.all()

    return render(request,'mi_app/mis_parientes.html',context)