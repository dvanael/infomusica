from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
# TABELA STATUS
class Status(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

# TABELA PERFIL
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=14)
    
    def __str__(self):
        return self.user.username

# TABELA SOLICITAÇÕES
class Solicitacao(models.Model):
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='status', to_field='id', default='1')
    usuario = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    justificativa = models.CharField(max_length=250, verbose_name='Justificativa', default='')
    data = models.DateField(default=timezone.now)
    hora = models.TimeField(default=timezone.now)
    post = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Solicitação de {} ({}) - {}".format(self.usuario, self.status, self.data)  
