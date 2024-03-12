from django.test import TestCase
from brain_ag.cultura.models import Cultura
from django.core.exceptions import ValidationError


class CulturaModelTest(TestCase):

    def test_nome_nao_pode_ser_vazio(self):
        """
        Testa se o nome da cultura não pode ser vazio.
        """
        with self.assertRaises(ValidationError) as error_context:
            Cultura(nome='').full_clean()
            self.assertIn('nome', error_context.exception.error_dict)
            self.assertEqual(
                error_context.exception.error_dict['nome'][0], 'Este campo não pode ficar em branco.')

    def test_ciclo_vida_nao_pode_ser_vazio(self):
        """
        Testa se o ciclo de vida da cultura não pode ser vazio.
        """
        with self.assertRaises(ValidationError) as error_context:
            Cultura(nome='Milho', ciclo_vida=None).full_clean()
            self.assertIn('ciclo_vida', error_context.exception.error_dict)
            self.assertEqual(
                error_context.exception.error_dict['ciclo_vida'][0], 'Ciclo de vida não pode ser vazio.')

    def test_epoca_plantio_pode_ser_vazio(self):
        """
        Testa se a época de plantio pode ser vazia.
        """
        cultura = Cultura.objects.create(nome='Feijão')
        self.assertIsNone(cultura.epoca_plantio)

    def test_irrigacao_necessaria_pode_ser_verdadeiro(self):
        """
        Testa se a irrigação necessária pode ser verdadeira.
        """
        cultura = Cultura.objects.create(
            nome='Trigo', irrigacao_necessaria=True)
        self.assertTrue(cultura.irrigacao_necessaria)

    def test_irrigacao_necessaria_pode_ser_falso(self):
        """
        Testa se a irrigação necessária pode ser falsa.
        """
        cultura = Cultura.objects.create(nome='Batata')
        self.assertFalse(cultura.irrigacao_necessaria)
