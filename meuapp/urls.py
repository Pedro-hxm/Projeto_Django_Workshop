from django.urls import path
from .views import listar_pessoas, criar_pessoa, atualiza_pessoa, deletar_pessoa

urlpatterns = [
    path('listar/', listar_pessoas, name = 'listar_pessoas'),
    path('criar/', criar_pessoa, name = 'criar_pessoa'),
    path('editar/<int:pk>' , atualiza_pessoa, name = 'atualizar_pessoa' ),
    path('deletar/<int:pk>' , deletar_pessoa, name = 'deletar_pessoa'),
]