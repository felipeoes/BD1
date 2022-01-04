from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from drugstore.views import *

router = routers.DefaultRouter()
router.register('clientes', ClientesViewSet, basename='Clientes')
router.register('clientes-telefones', ClientesTelefonesViewSet, basename='ClientesTelefones')
router.register('programa-beneficios', ProgramasBeneficiosViewSet, basename='ProgramaBeneficios')
router.register('funcionarios', FuncionariosViewSet, basename='Funcionarios')
router.register('funcionarios-telefones', FuncionariosTelefonesViewSet, basename='FuncionariosTelefones')
router.register('turnos', TurnosViewSet, basename='Turnos')
router.register('servicos', ServicosViewSet, basename='Servicos')
router.register('servicos-realizados', ServicosRealizadosViewSet, basename='ServicosRealizados')
router.register('compras', ComprasViewSet, basename='Compras')
router.register('produtos', ProdutosViewSet, basename='Produtos')
router.register('produtos-comprados', CompraProdutosViewSet, basename='ProdutosComprados')
router.register('fornecedores', FornecedoresViewSet, basename='Fornecedores')
router.register('fornecedores-telefones', FornecedoresTelefonesViewSet, basename='FornecedoresTelefones')
router.register('solicitacoes-produtos', SolicitacoesProdutosViewSet, basename='SolicitacoesProdutos')
router.register('top5-produtos', Top5ProdutosViewSet, basename='Top5Produtos')
router.register('top5-fornecedores', Top5FornecedoresViewSet, basename='Top5Fornecedores')
router.register('top5-funcionarios', Top5FuncionariosViewSet, basename='Top5Funcionarios')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),
    path('api/v1/usuarios/', include('users.urls')),
]
