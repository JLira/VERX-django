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
         db_table = 'brain_ag_produtor'
         verbose_name = 'Produtor'
         verbose_name_plural = 'Produtores'
         ordering = ['nome']

    def __str__(self):
        return self.nome


def criar_dados_mockados_produtor():
    # Criando dados mockados para Produtor
    if not Produtor.objects.exists():
        Produtor.objects.create(cpf="12345678901", nome="João da Silva")
        Produtor.objects.create(cpf="98765432109", nome="Maria Oliveira")
        Produtor.objects.create(cpf="23456789012", nome="Pedro Santos")
        Produtor.objects.create(cpf="89012345678", nome="Ana Souza")
        Produtor.objects.create(cpf="34567890123", nome="Luiza Pereira")

# Chamando a função para criar os dados mockados
criar_dados_mockados_produtor()
