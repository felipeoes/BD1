from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['cpf', 'nome', 'data_nascimento', 'email', 'sexo', 'id_beneficios']