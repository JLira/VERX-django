from django.contrib import admin

from brain_ag.produtor.models import Produtor

@admin.register(Produtor)
class ProdutorAdmin(admin.ModelAdmin):
    list_display = ('cpf','nome', 'dt_cadastro', 'dt_alteracao')
