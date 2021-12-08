from django.db.models import fields
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
    
    def validate(self, data):
        if not telefone_valido(data['telefone']):
            raise serializers.ValidationError({'telefone':"Número de telefone deve seguir o modelo: 1191234-1234 (respeitando o traço)"})
        return data

class ProgramaBeneficiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramaBeneficios
        fields = '__all__'
    
class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['funcional', 'nome', 'salario', 'sexo', 'sexo', 'tipo_func', 'crf']

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['funcional', 'nome', 'salario', 'sexo', 'sexo', 'tipo_func', 'crf']

class FuncionariosTelefonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuncionarioTelefones
        fields = '__all__'
    
    def validate(self, data):
        if not telefone_valido(data['telefone']):
            raise serializers.ValidationError({'celular':"Número de telefone deve seguir o modelo: 1191234-1234 (respeitando o traço)"})
        return data

class TurnosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = ['funcional', 'data_hora_entrada', 'data_hora_saida', 'descricao']
        
class ServicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = '__all__'
        
class ServicosRealizadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicoRealizado
        fields = '__all__'

class ComprasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = '__all__'
        
class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
        
    def validate(self, data):
        if not valor_valido(data['preco']):
            raise serializers.ValidationError({'preco':"O valor do produto deve ser positivo (maior que 0)"})
        return data

class CompraProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompraProduto
        fields = '__all__'
    
    def validate(self, data):
        if not valor_valido(data['quantidade']):
            raise serializers.ValidationError({'quantidade':"A quantidade vendida deve ser positiva (maior que 0)"})
        return data
    
class FornecedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'
    
    def validate(self, data):
        if not cnpj_valido(data['cnpj']):
            raise serializers.ValidationError({'cnpj':"Número de CPF inválido"})
        return data

class FornecedoresTelefonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FornecedorTelefones
        fields = '__all__'
    
    def validate(self, data):
        if not telefone_valido(data['telefone']):
            raise serializers.ValidationError({'telefone':"Número de telefone deve seguir o modelo: 1191234-1234 (respeitando o traço)"})
        return data

class SolicitacoesProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitacaoProduto
        fields = ['num_func', 'numero_pedido', 'codigo_barras', 'cnpj_forn', 'quantidade', 'valor_total']
    
    def validate(self, data):
        if not valor_valido(data['quantidade']):
            raise serializers.ValidationError({'quantidade':"A quantidade solicitada deve ser positiva (maior que 0)"})
        if not valor_valido(data['valor_total']):
            raise serializers.ValidationError({'valor_total':"O valor total deve ser positivo (maior que 0)"})
        return data