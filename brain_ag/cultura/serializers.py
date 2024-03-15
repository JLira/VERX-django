from rest_framework import serializers
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

from brain_ag.cultura.models import Cultura


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
   
