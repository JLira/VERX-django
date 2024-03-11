from uuid import uuid4
from django.db import models
from django.utils import timezone

from ..produtor.models import Produtor

class Fazenda(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    cnpj = models.CharField(max_length=14)
    nome = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=2)
    area_total = models.DecimalField(max_digits=10, decimal_places=2)
    area_agricultavel = models.DecimalField(max_digits=10, decimal_places=2)
    area_vegetacao = models.DecimalField(max_digits=10, decimal_places=2)
    dt_cadastro = models.DateTimeField(default=timezone.now)
    dt_alteracao = models.DateTimeField(auto_now=True)

    produtor = models.ManyToManyField(Produtor)

    class Meta:
        db_table = 'brain_ag_fazenda'
        verbose_name = 'Fazenda'
        verbose_name_plural = 'Fazendas'
        ordering = ['nome']
        
    def __str__(self):
        return self.nome