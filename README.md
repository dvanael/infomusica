<img src="static/img/infomusica-logotipo.png" alt="infomusica-logotipo" style="border-radius: 30px;">

## SOBRE
O INFOMUSICA é um sistema web para a difusão cultural da música no Campus IFRN SPP por meio deste. Visto a problemática de baixo interresse e pouco conhecimento dos eventos relacionados ao Laboratório de Práticas Musicais.

O projeto conta com :
- Sistema de agendamento e gerenciamento de reversas para o Laboratório de Práticas Musicais do campus ;
- Sistema de postagens relacionadas a música no campus e região ;
- Exibição do invetário de instrumentos presentes no laboratório.

Este projeto foi utilizado para a conclusão da matéria Projeto Integrador, que visa a aplicação práticas de todo o aprendizado adquirido nas matérias do curso integrado.

## TECNOLOGIAS UTILIZADAS
<div align="center">
  
![Django](https://img.shields.io/badge/-Django-0d1117?style=for-the-badge&logo=Django&logoColor=green)
![Python](https://img.shields.io/badge/-Python-0d1117?style=for-the-badge&logo=Python)
![HTML](https://img.shields.io/badge/-HTML5-0d1117?style=for-the-badge&logo=html5&logoColor) 
![CSS3](https://img.shields.io/badge/-CSS3-0d1117?style=for-the-badge&logo=css3&logoColor=blue) 
![JavaScript](https://img.shields.io/badge/-JavaScript-0d1117?style=for-the-badge&logo=javascript&logoColor) 
![Bootstrap](https://img.shields.io/badge/-Bootstrap-0d1117?style=for-the-badge&logo=bootstrap&logoColor)

</div>

## INSTALAÇÃO
**Instale as dependêcias.**
```bash
pip install -r requiriments.txt
```
---
**Definas as variavéis de sistema.**
- Crie um arquivo  `.env`
- Adicione as dependências no arquivo

**.env**
```
DEBUG = True
SECRET_KEY = 'sua_secret_key'

DEFAULT_FROM_EMAIL = 'seu_titulo'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587

EMAIL_HOST_USER = 'seu_email'
EMAIL_HOST_PASSWORD = 'sua_senha'
```
---
**Configure na sua máquina.**
- Faça as migrações necessárias.
```bash
python manage.py makemigrations
python manage.py migrate
```

- Crie um super usuário chamado `admin`
```bash
python manage.py createsuperuser
```
- Execute `python manage.py shell` para abrir o terminal interativo do Python
- Copie o código de `config.py`, cole no terminal, clique `Enter`

**config.py**
```py
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
```
- Todas as dependecias para executar o projeto foram concluídas!
  -
```bash
python manage.py runserver
```