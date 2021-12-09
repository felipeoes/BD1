from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm 
from .models import Usuario 
 
class CustomUserCreationForm(UserCreationForm):    
    class Meta:        
        model = Usuario        
        fields = ('email', 'funcional',)  
        
class CustomUserChangeForm(UserChangeForm):    
    class Meta:        
        model = Usuario        
        fields = UserChangeForm.Meta.fields