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
