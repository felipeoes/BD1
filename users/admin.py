from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
# from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import Usuario

class UsuarioAdmin(UserAdmin):    
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    # model = Usuario
    
    list_display = ('email', 'funcional','pk', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'funcional')
    # readonly_fields = ('date_joined', 'last_login')
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Usuario, UsuarioAdmin)