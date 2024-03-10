from uuid import uuid4
from django.db import models
from ..fazenda.models import Fazenda

class Culturas(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    culturas_plantadas = models.CharField(max_length=255)
    fazendas = models.ManyToManyField(Fazenda)

    def __str__(self):
        return self.culturas_plantadas