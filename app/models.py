from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from ckeditor.fields import RichTextField
    
class Profile(AbstractUser):
  username = models.EmailField(_('Email'), unique=True)
  matricula = models.CharField(_("Matrícula"), max_length=14, unique=True)
  profile_pic = models.ImageField(_("Foto de Perfil"), upload_to='profile_pics/', null=True, blank=True)

  REQUIRED_FIELDS = ['matricula']
  
  def __str__(self):
    return self.get_full_name()

  class Meta:
    ordering = ['-id']


class Solicitation(models.Model):
  CHOICES = (
     ('P', 'Pendente'),
     ('A', 'Aprovada'),
     ('R', 'Rejeitda'),
  )
    
  profile = models.ForeignKey("app.Profile", verbose_name=_("Perfil"), on_delete=models.PROTECT)
  justify = models.TextField(_('Justificativa'), default=None, max_length=250)
  justify_status = models.CharField(_('Justif. Status'), default=None, max_length=250, null=True, blank=True)
  date = models.DateField(_('Data'), default=timezone.now)
  entry_hour = models.TimeField(_('Hora de Entrada'), default=timezone.now)
  exit_hour = models.TimeField(_('Hora de Saída'), default=timezone.now)
  status = models.CharField(_("Status"), choices=CHOICES ,max_length=10, default='P')
  timestamp = models.DateTimeField(_('Timestamp'), auto_now=True, auto_now_add=False)

  def __str__(self):
    return "Solicitação de {} ({}) - {}".format(self.profile, self.get_status_display(), self.date)
  
  class Meta:
    ordering = ['-timestamp']


class Post(models.Model):
  title = models.CharField(_('Título'), default=None, max_length=150)
  content = RichTextField(_('Conteúdo'), default=None,)
  image = models.ImageField(_('Imagem de Capa'), upload_to='thumbnails/posts/' ,null=False, blank=False)
  author = models.ForeignKey(Profile, verbose_name='Autor', on_delete=models.PROTECT)
  timestamp = models.DateTimeField(_('Timestamp'), auto_now=True, auto_now_add=False)

  def __str__(self):
    return f'{self.title} por {self.author} - {self.timestamp.date()}'
    
  class Meta:
    ordering = ['-timestamp']

class Item(models.Model):
  name = models.CharField(default=None, max_length=100, verbose_name='Nome')
  description = models.TextField(default=None, max_length=550, verbose_name='Descrição')
  image = models.ImageField(null=True, blank=True, upload_to='thumbnails/itens/', verbose_name='Imagem')
  audio = models.FileField(null=True, blank=True, upload_to='documents/audio/', verbose_name='Amostra de Áudio')

  def __str__(self):
      return self.name
  
  class Meta:
    ordering = ['-id']