from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import Usuario

class UsuarioAdmin(UserAdmin):    
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Usuario
    list_display = ['email']

admin.site.register(Usuario, UsuarioAdmin)