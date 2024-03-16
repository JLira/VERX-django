from rest_framework import serializers
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

from brain_ag.cultura.models import Cultura
from brain_ag.fazenda.models import Fazenda
from brain_ag.produtor.models import Produtor


class ProdutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtor
        fields = '__all__'
        ref_name = 'ProdutorDetail'


class FazendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fazenda
        fields = '__all__'
        ref_name = 'FazendaDetail'


class CulturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cultura
        fields = (
            'id',
            'nome',
            'ciclo_vida',
            'epoca_plantio',
            'irrigacao_necessaria'
        )

