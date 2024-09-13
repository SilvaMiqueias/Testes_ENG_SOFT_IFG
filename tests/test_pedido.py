from django.test import TestCase
from pedido.models import Pedido
# Create your tests here.

class PedidoModelTest(TestCase):
        def setUp(self):
                  self.pedido = Pedido.objects.create(descrição="Teste", categoria=1)