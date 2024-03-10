from uuid import uuid4
from django.db import models
from ..produtor.models import Produtor

class Fazenda(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=2)
    area_total = models.DecimalField(max_digits=10, decimal_places=2)
    area_agricultavel = models.DecimalField(max_digits=10, decimal_places=2)
    area_vegetacao = models.DecimalField(max_digits=10, decimal_places=2)
    produtor = models.ManyToManyField(Produtor)

    def __str__(self):
        return self.nome