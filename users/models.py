from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    funcional = models.CharField(max_length=7)
    
    def __str__(self):
        return self.email