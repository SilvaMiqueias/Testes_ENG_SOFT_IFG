from django.test import TestCase
from categoria.models import Categoria
# Create your tests here.

class CategoriaModelTest(TestCase):

      def setUp(self):
          self.categoria = Categoria.objects.create(nome="Teste")

      def test_categoria_create(self):
          self.assertEqual(self.categoria.nome, "Teste")