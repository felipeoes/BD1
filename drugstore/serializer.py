from rest_framework import serializers
from .models import *
from .validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['cpf', 'nome', 'data_nascimento', 'email', 'sexo', 'id_beneficios']
        
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"Número de CPF inválido"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':"Nome deve conter apenas letras"})
        return data    
        

class ClienteTelefonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClienteTelefones
        fields = '__all__'
    
    def validate(telefone):
        if len(telefone) < 11:
            raise serializers.ValidationError("Telefone deve ter 11 dígitos")
        return telefone

class ProgramaBeneficiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramaBeneficios
        fields = '__all__'
    
class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['funcional', 'nome', 'salario', 'sexo', 'sexo', 'tipo_func', 'crf']