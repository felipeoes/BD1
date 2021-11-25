from rest_framework import viewsets, generics
from .models import Cliente
from .serializer import ClienteSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class ClientesViewSet(viewsets.ModelViewSet):
    """Exibindo todos os clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]