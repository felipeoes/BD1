from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm 
from .models import Usuario 
 
class CustomUserCreationForm(UserCreationForm):    
    class Meta:        
        model = Usuario        
        fields = ('email', 'funcional', 'last_login', 'date_joined', 'is_staff', 'first_name', 'last_name',)  
        
class CustomUserChangeForm(UserChangeForm):    
    class Meta:        
        model = Usuario        
        fields = UserChangeForm.Meta.fields