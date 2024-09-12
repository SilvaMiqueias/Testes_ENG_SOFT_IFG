from django.db import models
from categoria.models import Categoria  # Importa a Categoria

class Pedido(models.Model):
    descricao = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='pedidos')

    class Meta:
            db_table = 'pedido_pedido'

    def __str__(self):
        return self.descricao

