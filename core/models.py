from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
# Create your models here.


class Evento(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Evento')
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data da Criação')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    local = models.CharField(max_length=100, blank=True, null=True, verbose_name='Local do Evento')
    objects = models.Manager()

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%y às %H:%M:%S')

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False


    def get_evento_faltam(self):
        if datetime.now() < self.data_evento <= datetime.now() + timedelta(hours=1):
            return True
        else:
            return False

    def get_eventos_antigos(self):
        pass