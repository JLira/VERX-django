from rest_framework import serializers
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

from validate_docbr import CPF

from brain_ag.fazenda.models import Produtor

class ProdutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtor
        fields = (
            'id',
            'cpf',
            'nome'
        )
    
    def validate_cpf(self, valor):
        cpf = CPF()
        if not valor.isdigit():
            raise serializers.ValidationError('CPF deve conter apenas dígitos.')
        if len(valor) != 11:
            raise serializers.ValidationError('CPF deve ter 11 dígitos.')
        
        if not cpf.validate(valor):   
            raise serializers.ValidationError('CPF inválido.')
        
        return valor
