from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_auth.registration.serializers import RegisterSerializer
from .models import Usuario

class UserSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('email', 'funcional', 'last_login', 'date_joined', 'is_staff', 'first_name', 'last_name',)
        
class CustomRegisterSerializer(RegisterSerializer):
    primeiro_nome = serializers.CharField(max_length=30)
    ultimo_nome = serializers.CharField(max_length=30)
