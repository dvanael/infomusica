from django.contrib.auth.models import Group, User
from reserva.models import Status, Perfil

adminG, created = Group.objects.get_or_create(name='Admin')
alunoG, created = Group.objects.get_or_create(name='Aluno')

admin = User.objects.get(username='admin')
adminP, created = Perfil.objects.get_or_create(user=admin, matricula="00001")
admin.groups.add(adminG)

s1 = Status.objects.create(name='Pendente')
s2 = Status.objects.create(name='Rejeitada')
s3 = Status.objects.create(name='Aprovada')

exit()