from decimal import Decimal
from rest_framework import serializers
from django.core.exceptions import ValidationError

from validate_docbr import CNPJ

from .models import Fazenda


class FazendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fazenda
        fields = (
            'cnpj',
            'nome',
            'cidade',
            'estado',
            'area_total',
            'area_agricultavel',
            'area_vegetacao',
            'dt_cadastro',
            'dt_alteracao',
            'produtor'
        )

    def validate_cnpj(self, valor):
        cnpj = CNPJ()
        if not valor.isdigit():
            raise serializers.ValidationError(
                'CNPJ deve conter apenas dígitos.')
        if len(valor) != 14:
            raise serializers.ValidationError('CNPJ deve ter 14 dígitos.')

        if not cnpj.validate(valor):
            raise serializers.ValidationError('CNPJ inválido.')

        return valor

    def to_internal_value(self, data):
        # Armazena o dicionário de dados original
        original_data = data.copy()

        # Processa os dados (incluindo area_total se necessário)
        data = super().to_internal_value(data)

        return data

    def validate_area_total(self, data):
        area_total = data
        if not area_total:
            raise ValidationError({'area_total': 'Este campo é obrigatório.'})

        try:
            area_total = Decimal(area_total)
        except:
            raise ValidationError({'area_total': 'Valor inválido. Utilize apenas números.'})

        if area_total < 0:
            raise ValidationError({'area_total': 'O valor deve ser positivo.'})

        return area_total

    def validate(self, data):
        area_agricultavel = data.get('area_agricultavel')
        area_vegetacao = data.get('area_vegetacao')

        if area_agricultavel and not isinstance(area_agricultavel, Decimal):
            raise ValidationError({'area_agricultavel': 'Valor inválido. Utilize apenas números.'})

        if area_vegetacao and not isinstance(area_vegetacao, Decimal):
            raise ValidationError({'area_vegetacao': 'Valor inválido. Utilize apenas números.'})

        if area_agricultavel and area_vegetacao and area_agricultavel + area_vegetacao > data['area_total']:
            raise ValidationError({'area_total': 'A soma das áreas agricultável e de vegetação não pode ser maior que a área total.'})

        return data


    # def validate_area_total(self, data):
    #    area_total_hectares = data
    #    area_agricultavel_hectares = data['area_agricultavel']
    #    area_vegetacao_hectares = data['area_vegetacao']

    #    if area_agricultavel_hectares + area_vegetacao_hectares > area_total_hectares:
    #       raise ValidationError(
    #           'A soma da área agricultável e da vegetação não pode ser maior que a área total da fazenda.'
    #       )
    #    return data
