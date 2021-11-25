from django.db import models

class Cliente(models.Model):
    SEXO = (
        ('F', 'Feminino'),
        ('M', 'Masculino')
    )
    cpf = models.CharField(max_length=11, primary_key=True)
    nome = models.CharField(max_length=30)
    data_nascimento = models.DateField()
    email = models.EmailField(max_length=30)
    endereco = models.CharField(max_length= 50)
    sexo = models.CharField(max_length=1, choices=SEXO, blank=False, null=False)
    id_beneficios = models.CharField(max_length=2)
    
    class Meta:
        db_table = 'cliente'
        
    def __str__(self):
        return self.nome