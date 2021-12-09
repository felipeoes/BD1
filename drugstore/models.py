from enum import unique
from django.db import models

class Cliente(models.Model):
    SEXO = (
        ('F', 'Feminino'),
        ('M', 'Masculino')
    )
    cpf = models.CharField(max_length=11, primary_key=True)
    nome = models.CharField(max_length=30)
    data_nascimento = models.DateField(blank=True, null=True)
    email = models.EmailField(max_length=30, unique=True)
    endereco = models.CharField(max_length= 50, blank=True, null=True)
    sexo = models.CharField(max_length=1, choices=SEXO)
    id_beneficios = models.CharField(max_length=2)
    
    class Meta:
        db_table = 'cliente'
        
    def __str__(self):
        return self.nome
    
class ClienteTelefones(models.Model):
    cpf = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='cpf')
    telefone = models.CharField(max_length=11, primary_key=True)
    
    class Meta:
        db_table = 'cliente_telefones'
        
    def __str__(self):
        return (self.cpf + self.telefone)

class ProgramaBeneficios(models.Model):
    id = models.CharField(max_length=2, primary_key=True)
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.CharField(max_length=200, blank=True, null=True)
    fator_desconto = models.PositiveIntegerField(max_length=2)
    
    class Meta:
        db_table = 'programa_beneficios'
        
    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    SEXO = (
        ('F', 'Feminino'),
        ('M', 'Masculino')
    )
    funcional = models.CharField(max_length=7, primary_key=True)
    nome = models.CharField(max_length=30, unique=True)
    data_nascimento = models.DateField(blank=True, null=True)
    endereco = models.CharField(max_length= 50, blank=True, null=True)
    salario = models.FloatField(max_length=10)
    sexo = models.CharField(max_length=1, choices=SEXO)
    tipo_func = models.CharField(max_length=50)
    crf = models.CharField(max_length=6, unique=True, blank=True, null=True)
    
    class Meta:
        db_table = 'funcionario'
        
    def __str__(self):
        return self.funcional

class FuncionarioTelefones(models.Model):
    funcional = models.ForeignKey(Funcionario, on_delete=models.CASCADE, db_column='funcional')
    telefone = models.CharField(max_length=11, primary_key=True)
    
    class Meta:
        db_table = 'funcionario_telefones'
        
    def __str__(self):
        return (self.funcional + self.telefone)

class Turno(models.Model):
    funcional = models.ForeignKey(Funcionario, on_delete=models.CASCADE, db_column='funcional')
    data_hora_entrada = models.DateField(primary_key=True)
    data_hora_saida = models.DateField()
    descricao = models.CharField(max_length=200, blank=True, null=True)
    
    class Meta:
        db_table = 'turno'
        
    def __str__(self):
        return (self.funcional + self.data_hora_entrada)

class Servico(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    preco = models.FloatField(max_length=10)
    descricao = models.CharField(max_length=200, blank=True, null=True)
    nome = models.CharField(max_length=50, unique=True)
    
    
    class Meta:
        db_table = 'servico'
        
    def __str__(self):
        return self.id

class ServicoRealizado(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    id_servico = models.ForeignKey(Servico, on_delete=models.CASCADE, db_column='id_servico')
    cpf_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='cpf_cliente')
    num_func = models.ForeignKey(Funcionario, on_delete=models.CASCADE, db_column='num_func')
    data = models.DateField(blank=True, null=True)
    
    class Meta:
        db_table = 'servico_realizado'
        
    def __str__(self):
        return self.codigo

class Compra(models.Model):
    cpf_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='cpf_cliente')
    codigo_compra = models.CharField(max_length=9, primary_key=True)
    num_func = models.ForeignKey(Funcionario, on_delete=models.CASCADE, db_column='num_func')
    total = models.FloatField(max_length=10)
    data = models.DateField(blank=True, null=True)
    forma_pagamento = models.CharField(max_length=16)
    desconto = models.FloatField(max_length=10)
    
    
    class Meta:
        db_table = 'compra'
        
    def __str__(self):
        return self.codigo_compra

class Produto(models.Model):
    codigo_barras = models.CharField(max_length=12, primary_key=True)
    nome = models.CharField(max_length=50, unique=True)
    categoria = models.CharField(max_length=15)
    preco = models.FloatField(max_length=10)
    
    class Meta:
        db_table = 'produto'
        
    def __str__(self):
        return self.codigo_barras


class CompraProduto(models.Model):
    codigo_compra = models.ForeignKey(Compra, on_delete=models.CASCADE, primary_key=True, db_column='codigo_compra')
    codigo_barras = models.ForeignKey(Produto, on_delete=models.CASCADE, db_column='codigo_barras')
    quantidade = models.IntegerField()
    
    
    class Meta:
        db_table = 'compra_produto'
        
    def __str__(self):
        return (self.codigo_compra + self.codigo_barras)
    
class Fornecedor(models.Model):
    cnpj = models.CharField(max_length=14, primary_key=True)
    email = models.EmailField(max_length=30, unique=True)
    endereco = models.CharField(max_length=50, blank=True, null=True)
    razao_social = models.CharField(max_length=30, unique=True)
    
    class Meta:
        db_table = 'fornecedor'
        
    def __str__(self):
        return self.cnpj

class FornecedorTelefones(models.Model):
    cnpj_forn = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, db_column='cnpj_forn')
    telefone = models.CharField(max_length=11, primary_key=True)
    
    class Meta:
        db_table = 'fornecedor_telefones'
        
    def __str__(self):
        return (self.cnpj_forn + self.telefone)
    
class SolicitacaoProduto(models.Model):
    num_func = models.ForeignKey(Funcionario, on_delete=models.CASCADE, db_column='num_func')
    numero_pedido = models.CharField(max_length=10, primary_key=True)
    codigo_barras = models.ForeignKey(Produto, on_delete=models.CASCADE, db_column='codigo_barras') 
    cnpj_forn = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, db_column='cnpj_forn')
    quantidade = models.IntegerField()
    data_de_validade = models.DateField()
    data_solicitacao = models.DateField()
    valor_total = models.FloatField(max_length=10)
    
    class Meta:
        db_table = 'solicitacao_produto'
        
    def __str__(self):
        return self.numero_pedido