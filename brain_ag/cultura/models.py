from uuid import uuid4
from django.db import models
from django.forms import ValidationError

class Cultura(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=255)
    ciclo_vida = models.IntegerField(help_text='Dias para completar o ciclo de vida da cultura.', default=0, null=False)
    epoca_plantio = models.CharField(max_length=255, blank=True, null=True, help_text='Época ideal para o plantio da cultura.')
    irrigacao_necessaria = models.BooleanField(default=False)

    class Meta:
        db_table = 'brain_ag_cultura' 
        verbose_name = 'Cultura'
        verbose_name_plural = 'Culturas'
        ordering = ['nome']

    def clean(self):
       if not self.ciclo_vida:
           raise ValidationError("Ciclo de vida não pode ser vazio.")
     
    def __str__(self):
        return self.nome