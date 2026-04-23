from django.shortcuts import render, redirect
from .models import Dia, Palco, Concerto

def home_view(request):
    return render(request, 'festival/index.html')

def dias_view(request):
    context = {'dias': Dia.objects.all()}
    return render(request, 'festival/index.html', context)

def dia_view(request, dia_id):
    dia = Dia.objects.get(id=dia_id)
    concertos = Concerto.objects.filter(dia=dia)
    context = {
        'dia': dia,
        'concertos': concertos
    }
    return render(request, 'festival/index.html', context)

def palcos_view(request):
    context = {'palcos': Palco.objects.all()}
    return render(request, 'festival/palcos.html', context)

def concerto_view(request, concerto_id):
    concerto = Concerto.objects.get(id=concerto_id)
    return render(request, 'festival/concerto.html', {'concerto': concerto})

def edita_view(request, concerto_id):
    concerto = Concerto.objects.get(id=concerto_id)
    return render(request, 'festival/edita.html', {'concerto': concerto})

def apaga_view(request, concerto_id):
    concerto = Concerto.objects.get(id=concerto_id)
    concerto.delete()
    return redirect('festival:home')