from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento

# Create your views here.

# def index(request):
#     return redirect('/agenda/')

def retorna_local(request, titulo_evento):
    event = Evento.objects.get(titulo=titulo_evento)
    local = str(event.local)
    return HttpResponse('<h1>Local do Evento: {}</h1>'.format(local))


def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    response = {'eventos': evento}
    return render(request, 'agenda.html', response)