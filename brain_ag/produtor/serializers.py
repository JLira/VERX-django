from rest_framework import serializers
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

from validate_docbr import CPF

from brain_ag.fazenda.models import Fazenda, Produtor


class FazendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fazenda
        fields = '__all__'
        ref_name = 'FazendaDetail'


class ProdutorSerializer(serializers.ModelSerializer):
    fazendas = FazendaSerializer(many=True, read_only=True)
    class Meta:
        model = Produtor
        fields = '__all__'
        ref_name = 'ProdutorDetail'

    def validate_cpf(self, valor):
        cpf = CPF()
        if not valor.isdigit():
            raise serializers.ValidationError(
                'CPF deve conter apenas dígitos.')
        if len(valor) != 11:
            raise serializers.ValidationError('CPF deve ter 11 dígitos.')

        if not cpf.validate(valor):
            raise serializers.ValidationError('CPF inválido.')

        return valor
