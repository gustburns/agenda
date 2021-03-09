from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

# def index(request):
#     return redirect('/agenda/')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, message='Usuário e senha inválido')
            return redirect('/')
    else:
        return redirect('/')


def submit_logout(request):
    logout(request)
    return redirect('/')


def login_user(request):
    return render(request, 'login.html')


def retorna_local(request, titulo_evento):
    event = Evento.objects.get(titulo=titulo_evento)
    local = str(event.local)
    return HttpResponse('<h1>Local do Evento: {}</h1>'.format(local))


@login_required(login_url='/login')
def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    response = {'eventos': evento}
    return render(request, 'agenda.html', response)