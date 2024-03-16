from uuid import uuid4
from django.db import models
from django.forms import ValidationError

# from brain_ag.fazenda.models import Fazenda
class Cultura(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=255)
    ciclo_vida = models.IntegerField(help_text='Dias para completar o ciclo de vida da cultura.', default=0, null=False)
    epoca_plantio = models.CharField(max_length=255, blank=True, null=True, help_text='Época ideal para o plantio da cultura.')
    irrigacao_necessaria = models.BooleanField(default=False)
    # fazendas = models.ManyToManyField(Fazenda, related_name='culturas')

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
    
def criar_dados_mockados():
    if not Cultura.objects.exists():
        Cultura.objects.create(nome="Milho", ciclo_vida=90, epoca_plantio="Primavera", irrigacao_necessaria=True)
        Cultura.objects.create(nome="Trigo", ciclo_vida=120, epoca_plantio="Outono", irrigacao_necessaria=False)
        Cultura.objects.create(nome="Arroz", ciclo_vida=150, epoca_plantio="Verão", irrigacao_necessaria=True)
        Cultura.objects.create(nome="Feijão", ciclo_vida=80, epoca_plantio="Inverno", irrigacao_necessaria=False)
        Cultura.objects.create(nome="Soja", ciclo_vida=100, epoca_plantio="Primavera", irrigacao_necessaria=True)

# Chamando a função para criar os dados mockados
criar_dados_mockados()    