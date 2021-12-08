import re
from validate_docbr import CPF, CNPJ

def cpf_valido(num_cpf):
    cpf = CPF()
    return cpf.validate(num_cpf)

def cnpj_valido(num_cnpj):
    cnpj = CPF()
    return cnpj.validate(num_cnpj)

def nome_valido(nome):
    return nome.isalpha()

def telefone_valido(num_telefone):
    """Valida o celular seguindo o formato (1191234-1234)"""
    regex = '[0-9]{2}[0-9]{5}-[0-9]{4}'
    match = re.findall(regex, num_telefone)
    return match

def valor_valido(preco):
    return preco > 0