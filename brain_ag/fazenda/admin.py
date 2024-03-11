from django.contrib import admin

from .models import Fazenda
from ..produtor.models import Produtor


@admin.register(Fazenda)
class FazendaAdmin(admin.ModelAdmin):
    def produtor_lookup(self, obj):
        return ', '.join([produtor.nome for produtor in obj.produtor.all()])
    
    list_display = ('cnpj','nome','cidade','estado','area_total','area_agricultavel','area_vegetacao','produtor_lookup')
