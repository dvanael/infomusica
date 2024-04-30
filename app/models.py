from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
    
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