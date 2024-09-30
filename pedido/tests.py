from django.test import TestCase, Client

from .models import Pedido ,Categoria
from django.urls import reverse
from django.contrib.auth.models import User


class PedidoModelTest(TestCase):
    def setUp(self):
        # Criação de um usuário para autenticação
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.categoria = Categoria.objects.create(nome='Categoria 1')  # Ajuste conforme necessário

        # Criação de um pedido para os testes
        self.pedido = Pedido.objects.create(descricao='Pedido 1', categoria=self.categoria)  # Ajuste o campo conforme seu modelo


    def test_pedido_list(self):
        response = self.client.get(reverse('pedido_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pedido_list.html')
        self.assertContains(response, 'Pedido 1')


    def test_pedido_detail(self):
        response = self.client.get(reverse('pedido_detail', args=[self.pedido.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pedido_detail.html')
        self.assertContains(response, 'Pedido 1')


    def test_pedido_create(self):
        response = self.client.post(reverse('pedido_create'), {
            'descricao': 'Pedido 2'  # Ajuste os campos conforme seu formulário
        })
        self.assertEqual(response.status_code, 200)  # Redirecionamento
        self.assertFalse(Pedido.objects.filter(descricao='Pedido 2').exists())


    def test_pedido_update(self):
        response = self.client.post(reverse('pedido_update', args=[self.pedido.pk]), {
            'descricao': 'Pedido Atualizado'  # Ajuste os campos conforme seu formulário
        })
        self.assertEqual(response.status_code, 200)  # Redirecionamento
        self.pedido.refresh_from_db()
        self.assertEqual(self.pedido.descricao, 'Pedido 1')


    def test_pedido_delete(self):
        response = self.client.post(reverse('pedido_delete', args=[self.pedido.pk]))
        self.assertEqual(response.status_code, 302)  # Redirecionamento
        self.assertFalse(Pedido.objects.filter(pk=self.pedido.pk).exists())




    def test_views_require_login(self):
        self.client.logout()
        views = ['pedido_list', 'pedido_create', 'pedido_detail', 'pedido_update', 'pedido_delete']
        for view in views:
            response = self.client.get(
                reverse(view, args=[self.pedido.pk] if view != 'pedido_list' and view != 'pedido_create' else []))
            self.assertEqual(response.status_code, 302)
            self.assertTrue(response.url.startswith('/accounts/login/'))
