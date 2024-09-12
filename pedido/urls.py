from django.urls import path
from . import views

urlpatterns = [
    path('', views.pedido_list, name='pedido_list'),
    path('<int:pk>/', views.pedido_detail, name='pedido_detail'),
    path('criar/', views.pedido_create, name='pedido_create'),
    path('<int:pk>/atualizar/', views.pedido_update, name='pedido_update'),
    path('<int:pk>/deletar/', views.pedido_delete, name='pedido_delete'),
]
