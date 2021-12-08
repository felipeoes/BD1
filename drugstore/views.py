from rest_framework import viewsets, filters
from .models import Cliente
from .serializer import *
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class ClientesViewSet(viewsets.ModelViewSet):
    """Exibindo todos os clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ClientesTelefonesViewSet(viewsets.ModelViewSet):
    """Exibindo todos os telefones dos clientes"""
    queryset = ClienteTelefones.objects.all()
    serializer_class = ClienteTelefonesSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ProgramasBeneficiosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os programas de benefícios"""
    queryset = ProgramaBeneficios.objects.all()
    serializer_class = ProgramaBeneficiosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class FuncionariosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os funcionarios"""
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class FuncionariosTelefonesViewSet(viewsets.ModelViewSet):
    """Exibindo todos os telefones dos funcionarios"""
    queryset = FuncionarioTelefones.objects.all()
    serializer_class = FuncionariosTelefonesSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class TurnosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os turnos"""
    queryset = Turno.objects.all()
    serializer_class = TurnosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ServicosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os servicos"""
    queryset = Servico.objects.all()
    serializer_class = ServicosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ServicosRealizadosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os servicos realizados"""
    queryset = ServicoRealizado.objects.all()
    serializer_class = ServicosRealizadosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ComprasViewSet(viewsets.ModelViewSet):
    """Exibindo todas os compras"""
    queryset = Compra.objects.all()
    serializer_class = ComprasSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class ProdutosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os produtos"""
    queryset = Produto.objects.all()
    serializer_class = ProdutosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CompraProdutosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os produtos de uma compra"""
    queryset = CompraProduto.objects.all()
    serializer_class = CompraProdutosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class FornecedoresViewSet(viewsets.ModelViewSet):
    """Exibindo todos os fornecedores"""
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedoresSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class FornecedoresTelefonesViewSet(viewsets.ModelViewSet):
    """Exibindo todos os telefones dos fornecedores"""
    queryset = FornecedorTelefones.objects.all()
    serializer_class = FornecedoresTelefonesSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class SolicitacoesProdutosViewSet(viewsets.ModelViewSet):
    """Exibindo todos as solicitações de produtos"""
    queryset = SolicitacaoProduto.objects.all()
    serializer_class = SolicitacoesProdutosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]