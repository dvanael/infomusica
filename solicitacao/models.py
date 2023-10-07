from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
#CRUD DE USUARIO
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=14)
    
    def __str__(self):
        return self.user.username

#CRUD SOLICITAÇÕES
class Solicitacao(models.Model):
    class Status(models.TextChoices):
        PENDENTE = 'PEN', 'Pendente'
        APROVADA = 'APR', 'Aprovada'
        REJEITADA = 'REJ', 'Rejeitada'

    status = models.CharField(max_length=3, choices=Status.choices, default=Status.PENDENTE)

    usuario = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=14, blank=True, null=True)
    justificativa = models.CharField(max_length=250, verbose_name='Justificativa', default='')
    data = models.DateField(default=timezone.now)
    hora = models.TimeField(default=timezone.now)
    post = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.matricula = self.usuario.matricula
        super(Solicitacao, self).save(*args, **kwargs)

    def __str__(self):
        return "{} ({}) - {}".format(self.usuario, self.status, self.data)  
