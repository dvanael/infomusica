from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date
from ckeditor.fields import RichTextField

# Create your models here.
# TABELA STATUS
class Status(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

# TABELA PERFIL
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuario')
    matricula = models.CharField(max_length=14, unique=True, verbose_name='Matrícula')
    
    def __str__(self):
        return self.user.username

# TABELA SOLICITAÇÕES
class Solicitacao(models.Model):
    status = models.ForeignKey(Status, on_delete=models.CASCADE,verbose_name='Status', related_name='status', to_field='id', default='1')
    profile = models.ForeignKey(Perfil, on_delete=models.CASCADE, verbose_name='Perfil')
    justificativa = models.CharField(default='', max_length=250, verbose_name='Justificativa')
    justify_status = models.CharField(default='Ainda não justificado.', max_length=250, verbose_name='Justificativa Status')
    data = models.DateField(default=date.today, verbose_name='Data')
    entry_hour = models.TimeField(default=timezone.now, verbose_name='Hora de Entrada')
    exit_hour = models.TimeField(default=timezone.now, verbose_name='Hora de Saída')
    post = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Post')

    def __str__(self):
        return "Solicitação de {} ({}) - {}".format(self.profile, self.status, self.data)  
    
# TABELA ITEM
class Item(models.Model):
    name = models.CharField(default='', max_length=100, verbose_name='Nome')
    description = models.TextField(default='', max_length=250, verbose_name='Descrição')
    image = models.ImageField(null=True, blank=True, upload_to='images/', verbose_name='Imagem')
    sound = models.FileField(null=True, blank=True, upload_to='documents/', verbose_name='Amostra de Áudio')

    def __str__(self):
        return self.name

# TABELA POST
class Post(models.Model):
    title = models.CharField(default='', max_length=150, verbose_name='Título')
    content = RichTextField(default='', verbose_name='Conteúdo')
    image = models.ImageField(null=False, blank=False, verbose_name='Imagem')
    author = models.ForeignKey(Perfil, on_delete=models.CASCADE,  verbose_name='Autor')
    post = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Post')

    def __str__(self):
        return self.title

