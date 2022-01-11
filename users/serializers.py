from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
# from rest_auth.registration.serializers import RegisterSerializer
from django.utils.translation import gettext_lazy as _
from .models import Usuario, upload_to


def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)


class UserRegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Usuario
        fields = ['funcional', 'username', 'email', 'first_name', 'last_name',
                  'password', 'password2', 'profile_image']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def save(self, request, *args, **kwargs):
        user = Usuario(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            funcional=self.validated_data['funcional'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            profile_image=self.validated_data['profile_image'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user

# class UserSerializer(ModelSerializer):
#     class Meta:
#         model = Usuario
#         fields = ('email', 'funcional', 'profile_image', 'last_login',
#                   'date_joined', 'is_staff', 'first_name', 'last_name',)


# class CustomRegisterSerializer(RegisterSerializer):
#     first_name = serializers.CharField(max_length=30)
#     last_name = serializers.CharField(max_length=30)
#     funcional = serializers.CharField(max_length=7)
#     # profile_image = serializers.ImageField(
#     #     _("Image"), upload_to=upload_to, default='posts/user_default.png')

#     def get_cleaned_data(self):
#         data_dict = super().get_cleaned_data()
#         data_dict['first_name'] = self.validated_data.get('first_name', '')
#         data_dict['last_name'] = self.validated_data.get('last_name', '')
#         data_dict['funcional'] = self.validated_data.get('funcional', '')
#         data_dict['profile_image'] = self.validated_data.get('profile_image', '')
#         return data_dict
