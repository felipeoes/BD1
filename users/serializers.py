from rest_framework.serializers import ModelSerializer
from .models import Usuario
class UserSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('email', 'funcional', 'last_login', 'date_joined', 'is_staff')