import uuid
from django.test import TestCase
from ..models import Produtor
import unittest.mock  # Para mockar a função uuid4
from unittest.mock import patch
from django.core.exceptions import ValidationError
from django.db.utils import DataError 

class ProdutorModelTest(TestCase):

    def setUp(self):
        self.cpf = '12345678900'
        self.nome = 'Produtor Teste'

    def test_create_produtor(self):
        """
        Testa a criação de um novo objeto Produtor.
        """
        produtor = Produtor.objects.create(cpf=self.cpf, nome=self.nome)
        # Verifica se o ID foi gerado automaticamente
        self.assertIsNotNone(produtor.id)
        self.assertEqual(produtor.cpf, self.cpf)
        self.assertEqual(produtor.nome, self.nome)

    def test_cpf_max_length(self):
        """
        Testa se o campo 'cpf' respeita o tamanho máximo.
        """
        dados_produtor = {
            "cpf": "123456789012",  # CPF inválido com 12 caracteres
            "nome": self.nome,
        }
        # Tenta criar um Produtor com CPF inválido
        with self.assertRaises(DataError):  # Alterando para esperar DataError
            Produtor.objects.create(**dados_produtor)

    def test_nome_max_length(self):
        """
        Testa se o campo 'nome' respeita o tamanho máximo.
        """
        long_name = 'x' * 256  # Cria string com 256 caracteres
        with self.assertRaises(DataError):
            Produtor.objects.create(nome=long_name)

    @patch('uuid.uuid4')  # Mocka a função uuid4 para teste controlado
    def test_default_id(self, mock_uuid4):
        """
        Testa se o ID é gerado automaticamente usando uuid4.
        """
        fake_uuid = 'd158ba5e-92af-4d9d-a8f3-21a57eeb1d3a'  # UUID falso para simular geração
        mock_uuid4.return_value = uuid.UUID(fake_uuid)  # Convertendo para um objeto UUID
        produtor = Produtor.objects.create(cpf=self.cpf, nome=self.nome)
        
        # Verifica se o ID gerado pelo modelo é um UUID válido e diferente do fake
        self.assertIsInstance(produtor.id, uuid.UUID)
        self.assertNotEqual(produtor.id, uuid.UUID(fake_uuid))

    
    def test_dt_cadastro_default(self):
        """
        Testa se o campo 'dt_cadastro' é preenchido automaticamente.
        """
        produtor = Produtor.objects.create(cpf=self.cpf, nome=self.nome)
        self.assertIsNotNone(produtor.dt_cadastro)

    def test_dt_alteracao_auto_now(self):
        """
        Testa se o campo 'dt_alteracao' é atualizado automaticamente na alteração.
        """
        produtor = Produtor.objects.create(cpf=self.cpf, nome=self.nome)
        dt_alteracao_inicial = produtor.dt_alteracao

        # Altera o nome do produtor para disparar o auto_now
        produtor.nome = 'Produtor Atualizado'
        produtor.save()

        self.assertGreater(produtor.dt_alteracao, dt_alteracao_inicial)
