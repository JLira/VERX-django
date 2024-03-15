from django.contrib import admin

from brain_ag.cultura.models import Cultura


@admin.register(Cultura)
class CulturaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nome',
        'ciclo_vida',
        'epoca_plantio',
        'irrigacao_necessaria')
