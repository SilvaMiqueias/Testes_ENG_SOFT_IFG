from django import forms
from .models import Pedido
from categoria.models import Categoria

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['descricao', 'categoria']
