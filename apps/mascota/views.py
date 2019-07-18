from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.mascota.forms import MascotaForm
from apps.mascota.models import Mascota

def index(request):
    return render(request, 'mascota/index.html')

def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mascota:index')
    else:
        form = MascotaForm()
    return render(request, 'mascota/mascota_form.html', {'form':form})

def mascota_list(request):
    mascotas = Mascota.objects.all().order_by('folio')
    contexto = {'mascotas':mascotas}
    return render(request, 'mascota/mascota_list.html', contexto)

def mascota_edit(request, id_mascota):
    mascota = Mascota.objects.get(folio=id_mascota)
    if request.method == 'GET':
        form = MascotaForm(instance = mascota)
    else:
        form = MascotaForm(request.POST, instance = mascota)
        if form.is_valid():
            form.save()
        return redirect('mascota:lista_mascota')
    return render(request, 'mascota/mascota_form.html', {'form': form})

def mascota_delete(request, id_mascota):
    mascota = Mascota.objects.get(folio = id_mascota)
    if request.method == 'POST':
        mascota.delete()
        return redirect('mascota:lista_mascota')
    return render(request, 'mascota/mascota_delete.html', {'mascota':mascota})