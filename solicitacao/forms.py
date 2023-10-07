from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Solicitacao, Perfil

# USUARIO FORM
class UsuarioForm(UserCreationForm):
    email = forms.EmailField(max_length = 100)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']    

    def clean_email(self):
        e = self.cleaned_data['email']
        if User.objects.filter(email = e).exists():
            raise ValidationError(f"O email {e} já está em uso.") 
        return e
    
class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['matricula']


# AJAX SOLICITACAO FORM
class EventoForm(forms.ModelForm):
    class Meta:
        model = Solicitacao
        fields = ('justificativa', 'data', 'hora')
