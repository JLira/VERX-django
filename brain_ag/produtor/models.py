from uuid import uuid4
from django.db import models
from django.utils import timezone

class Produtor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=255)

    dt_cadastro = models.DateTimeField(default=timezone.now)
    dt_alteracao = models.DateTimeField(auto_now=True)

    class Meta:
         verbose_name = 'Produtor'
         verbose_name_plural = 'Produtores'
         ordering = ['nome']

    def __str__(self):
        return self.nome


