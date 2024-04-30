from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from app.models import Profile 

# Cadastro Usuario Form
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'matricula')
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
        }

    def clean_email(self):
        email = self.cleaned_data['username']
        if Profile.objects.filter(username=email).exists():
            raise ValidationError(f"O email {email} já está em uso.") 
        return email
    
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        email = self.fields['username']
        first_name =  self.fields['first_name']
        last_name =  self.fields['last_name']
        password1 = self.fields['password1']
        password2 = self.fields['password2']
        matricula = self.fields['matricula']

        first_name.widget.attrs={'placeholder': 'Digite seu Primeiro Nome'}
        last_name.widget.attrs={'placeholder': 'Digite seu Sobrenome'}
        
        email.widget.attrs={'placeholder': 'Digite seu email'}
        email.help_text = ''
        
        password1.widget.attrs={'placeholder': 'Digite sua senha'}
        password1.help_text = ''

        password2.widget.attrs={'placeholder': 'Confirme sua senha'}
        password2.help_text = ''

        matricula.widget.attrs={'placeholder': 'Digite sua matrícula'}

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = Profile
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        email =  self.fields['username']
        password = self.fields['password']
        email.widget.attrs={
            'placeholder': 'Digite seu email',
            'autofocus': True,
        }
        password.widget.attrs={'placeholder': 'Digite sua senha'}