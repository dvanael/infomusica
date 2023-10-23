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
class SolicitacaoForm(forms.ModelForm):
    class Meta:
        model = Solicitacao
        fields = ('justificativa', 'data', 'hora')
        widgets = {
            "data": forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'},
                format="%d-%m-%Y",
            ),
            "hora": forms.TimeInput(
                attrs={'type': 'time', 'class': 'form-control'},
                format="%H:%M",
            ),
        }

class StatusForm(forms.ModelForm):
    class Meta:
        model = Solicitacao
        fields = ('status', 'justificativa')
