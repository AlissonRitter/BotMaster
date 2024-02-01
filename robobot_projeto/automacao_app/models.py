from django.db import models

# Create your models here.
# automacao_app/models.py
from django.db import models

class ConfiguracaoAutomacao(models.Model):
    hora_inicio = models.TimeField()
    hora_termino = models.TimeField()
    ativa = models.BooleanField(default=False)

    def __str__(self):
        return f'Configuração: {self.hora_inicio} - {self.hora_termino}'
