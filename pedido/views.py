from django.shortcuts import render, get_object_or_404, redirect
from .models import Pedido
from .forms import PedidoForm
from django.contrib.auth.decorators import login_required


@login_required
def pedido_list(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedido_list.html', {'pedidos': pedidos})

@login_required
def pedido_detail(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    return render(request, 'pedido_detail.html', {'pedido': pedido})

@login_required
def pedido_create(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pedido_list')
    else:
        form = PedidoForm()
    return render(request, 'pedido_form.html', {'form': form})

@login_required
def pedido_update(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('pedido_list')
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'pedido_form.html', {'form': form})

@login_required
def pedido_delete(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        pedido.delete()
        return redirect('pedido_list')
    return render(request, 'pedido_confirm_delete.html', {'pedido': pedido})
