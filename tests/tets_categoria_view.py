from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Categoria
from .forms import Categoria
from .views import Categoria

class CategoriaViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.categoria = Categoria.objects.create(nome='Teste Categoria')
        self.client.login(username='testuser', password='12345')

    def test_categoria_list_view(self):
        response = self.client.get(reverse('categoria_list'))
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, 'categoria_list.html')
        self.assertContains(response, 'Teste Categoria')

    def test_categoria_detail_view(self):
        response = self.client.get(reverse('categoria_detail', args=[self.categoria.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, 'categoria_detail.html')
        self.assertContains(response, 'Teste Categoria')

    def test_categoria_create_view_get(self):
        response = self.client.get(reverse('categoria_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'categoria_form.html')
        self.assertIsInstance(response.context['form'], categoria_form)

    def test_categoria_create_view_post(self):
        response = self.client.post(reverse('categoria_create'), data={'nome': 'Nova Categoria'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('categoria_list'))
        self.assertTrue(Categoria.objects.filter(nome='Nova Categoria').exists())

    def test_categoria_update_view_get(self):
        response = self.client.get(reverse('categoria_update', args=[self.categoria.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, 'categoria_form.html')
        self.assertIsInstance(response.context['form'], categoria_form)

    def test_categoria_update_view_post(self):
        response = self.client.post(reverse('categoria_update', args=[self.categoria.pk]), data={'nome': 'Categoria Atualizada'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('categoria_list'))
        self.categoria.refresh_from_db()
        self.assertEqual(self.categoria.nome, 'Categoria Atualizada')

    def test_categoria_delete_view_get(self):
        response = self.client.get(reverse('categoria_delete', args=[self.categoria.pk]))
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'categoria_confirm_delete.html')

    def test_categoria_delete_view_post(self):
        response = self.client.post(reverse('categoria_delete', args=[self.categoria.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('categoria_list'))
        self.assertFalse(Categoria.objects.filter(pk=self.categoria.pk).exists())

    def test_views_require_login(self):
        self.client.logout()
        views = ['categoria_list', 'categoria_create', 'categoria_detail', 'categoria_update', 'categoria_delete']
        for view in views:
            response = self.client.get(reverse(view, args=[self.categoria.pk] if view != 'categoria_list' and view != 'categoria_create' else []))
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.url.startswith('/accounts/login/'))


