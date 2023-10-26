from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
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
    
    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs={'placeholder': 'Digite um nome de usuário'}
        self.fields['email'].widget.attrs={'placeholder': 'Digite um e-mail válido'}
        self.fields['password1'].widget.attrs={'placeholder': 'Digite uma senha'}
        self.fields['password2'].widget.attrs={'placeholder': 'Confirme sua senha'}
    
class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['matricula']
        widgets = {
            'matricula': forms.TextInput(attrs={'placeholder': 'Digite sua matrícula'}),
        }

class ProfileEditForm(UserChangeForm):
    email = forms.EmailField(max_length=100)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    # Personalização das mensagens de ajuda diretamente no formulário
    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['email'].help_text = ''
        self.fields['password'].widget = forms.HiddenInput()

# AJAX SOLICITACAO FORM
class SolicitacaoForm(forms.ModelForm):
    class Meta:
        model = Solicitacao
        fields = ('justificativa', 'data', 'hora')
        widgets = {
            "data": forms.DateInput(format = ('%Y-%m-%d'), attrs = {'type': 'date', 'class': 'form-control'}),
            "hora": forms.TimeInput(format = "%H:%M", attrs = {'type': 'time', 'class': 'form-control'}),
            'justificativa': forms.TextInput(attrs={'placeholder': 'Justifique sua solicitação'})
        }

class StatusForm(forms.ModelForm):
    class Meta:
        model = Solicitacao
        fields = ('status', 'justificativa')
