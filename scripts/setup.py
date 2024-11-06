import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

import django

django.setup()

from django.contrib.auth.models import Group, User
from reserva.models import Status, Perfil

username = "admin"
password = "senha"
full_name = "Administrador"

a = User.objects.create_superuser(
    username=username, password=password, first_name=full_name
)
a.save()

print(" \nYour super user has been created.")
print(
    f"Login with \n \nusername: {username} \npassword: {password} \n \nATTENTION: Dont lose these credentials."
)

adminG, created = Group.objects.get_or_create(name='Admin')
alunoG, created = Group.objects.get_or_create(name='Aluno')

admin = User.objects.get(username='admin')
adminP, created = Perfil.objects.get_or_create(user=admin, matricula="00001")
admin.groups.add(adminG)

s1 = Status.objects.create(name='Pendente')
s2 = Status.objects.create(name='Rejeitada')
s3 = Status.objects.create(name='Aprovada')

exit()