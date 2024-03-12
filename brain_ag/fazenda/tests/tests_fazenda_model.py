from django.test import TestCase
from django.core.exceptions import ValidationError
from brain_ag.fazenda.models import Fazenda

class FazendaModelTest(TestCase):

    def test_cnpj_nao_pode_ser_vazio(self):
        """
        Testa se o CNPJ da fazenda não pode ser vazio.
        """
        with self.assertRaises(ValidationError) as error_context:
            fazenda = Fazenda(cnpj='', nome='Fazenda Teste', cidade='Cidade', estado='UF', area_total=100, area_agricultavel=50, area_vegetacao=20)
            fazenda.full_clean()  # Aplicar validação do modelo
            fazenda.save()  # Salvar fazenda no banco de dados
        self.assertIn('cnpj', error_context.exception.error_dict)
        #self.assertEqual(error_context.exception.error_dict['cnpj'][0], 'Este campo não pode ficar em branco.')
    
    def test_nome_nao_pode_ser_vazio(self):
        """
        Testa se o nome da fazenda não pode ser vazio.
        """
        with self.assertRaises(ValidationError) as error_context:
            Fazenda(cnpj='12345678901234', nome='', cidade='Cidade', estado='UF', area_total=100, area_agricultavel=50, area_vegetacao=20).full_clean()
        self.assertIn('nome', error_context.exception.error_dict)
        self.assertNotEqual(error_context.exception.error_dict['nome'][0], 'Este campo não pode estar vazio.')
        

    def test_cidade_nao_pode_ser_vazia(self):
        """
        Testa se a cidade da fazenda não pode ser vazia.
        """
        with self.assertRaises(ValidationError) as error_context:
            Fazenda(cnpj='12345678901234', nome='Fazenda Teste', cidade='', estado='UF', area_total=100, area_agricultavel=50, area_vegetacao=20).full_clean()
        self.assertIn('cidade', error_context.exception.error_dict)
        self.assertNotEqual(error_context.exception.error_dict['cidade'][0], 'Este campo não pode ficar em branco.')

    def test_estado_nao_pode_ser_vazio(self):
        """
        Testa se o estado da fazenda não pode ser vazio.
        """
        with self.assertRaises(ValidationError) as error_context:
            Fazenda(cnpj='12345678901234', nome='Fazenda Teste', cidade='Cidade', estado='', area_total=100, area_agricultavel=50, area_vegetacao=20).full_clean()
        self.assertIn('estado', error_context.exception.error_dict)
        self.assertNotEqual(error_context.exception.error_dict['estado'][0], 'Este campo não pode ficar em branco.')

    def test_area_total_nao_pode_ser_vazia(self):
        """
        Testa se a área total da fazenda não pode ser vazia.
        """
        with self.assertRaises(ValidationError) as error_context:
            Fazenda(cnpj='12345678901234', nome='Fazenda Teste', cidade='Cidade', estado='UF', area_total=None, area_agricultavel=50, area_vegetacao=20).full_clean()
        self.assertIn('area_total', error_context.exception.error_dict)
        self.assertNotEqual(error_context.exception.error_dict['area_total'][0], 'Este campo não pode ficar em branco.')

    def test_area_agricultavel_nao_pode_ser_vazia(self):
        """
        Testa se a área agricultável da fazenda não pode ser vazia.
        """
        with self.assertRaises(ValidationError) as error_context:
            fazenda = Fazenda(cnpj='12345678901234', nome='Fazenda Teste', cidade='Cidade', estado='UF', area_total=100, area_vegetacao=20)
            fazenda.full_clean()  # Aplicar validação do modelo
            fazenda.save()  # Salvar fazenda no banco de dados
        self.assertIn('area_agricultavel', error_context.exception.error_dict)
        self.assertNotEqual(error_context.exception.error_dict['area_agricultavel'][0], 'Este campo não pode ficar em branco.')

    def test_area_vegetacao_nao_pode_ser_vazia(self):
        """
        Testa se a área de vegetação da fazenda não pode ser vazia.
        """
        with self.assertRaises(ValidationError) as error_context:
            Fazenda(cnpj='12345678901234', nome='Fazenda Teste', cidade='Cidade', estado='UF', area_total=100, area_agricultavel=50, area_vegetacao=None).full_clean()
        self.assertIn('area_vegetacao', error_context.exception.error_dict)
        self.assertNotEqual(error_context.exception.error_dict['area_vegetacao'][0], 'Este campo não pode ficar em branco.')
