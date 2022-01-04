from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_auth.registration.serializers import RegisterSerializer
from .models import Usuario

class UserSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('email', 'funcional', 'last_login', 'date_joined', 'is_staff', 'first_name', 'last_name',)

class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    funcional = serializers.CharField(max_length=7)
    
    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['first_name'] = self.validated_data.get('first_name', '')
        data_dict['last_name'] = self.validated_data.get('last_name', '')
        data_dict['funcional'] = self.validated_data.get('funcional', '')
        return data_dict