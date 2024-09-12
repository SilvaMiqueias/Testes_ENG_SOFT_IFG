from django.urls import path
from . import views

urlpatterns = [
    path('', views.categoria_list, name='categoria_list'),
    path('<int:pk>/', views.categoria_detail, name='categoria_detail'),
    path('criar/', views.categoria_create, name='categoria_create'),
    path('<int:pk>/atualizar/', views.categoria_update, name='categoria_update'),
    path('<int:pk>/deletar/', views.categoria_delete, name='categoria_delete'),
]
