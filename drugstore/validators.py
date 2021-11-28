import re
from validate_docbr import CPF

def cpf_valido(num_cpf):
    cpf = CPF()
    return cpf.validate(num_cpf)

def nome_valido(nome):
    return nome.isalpha()