![INFOMUSICA](static/img/infomusica-logotipo.png)

# INFOMUSICA

## SOBRE

O Infomusica é um sistema web para a difusão cultural da música no Campus IFRN SPP por meio deste. Visto a problemática de baixo interresse e pouco conhecimento dos eventos relacionados ao Laboratório de Práticas Musicais.

O projeto conta com :
- Sistema de agendamento e gerenciamento de reversas para o Laboratório de Práticas Musicais do campus ;

- Sistema de postagens relacionadas a música no campus e região ;

- Exibição do invetário de instrumentos presentes no laboratório.

Este projeto foi utilizado para a conclusão da matéria Projeto Integrador, que visa a aplicação práticas de todo o aprendizado adquirido nas matérias do curso integrado.

---

## TECNOLOGIAS UTILIZADAS

![Django](https://img.shields.io/badge/-Django-0d1117?style=for-the-badge&logo=Django&logoColor=green)
![Python](https://img.shields.io/badge/-Python-0d1117?style=for-the-badge&logo=Python)
![HTML](https://img.shields.io/badge/-HTML5-0d1117?style=for-the-badge&logo=html5&logoColor)
![CSS3](https://img.shields.io/badge/-CSS3-0d1117?style=for-the-badge&logo=css3&logoColor=blue)
![JavaScript](https://img.shields.io/badge/-JavaScript-0d1117?style=for-the-badge&logo=javascript&logoColor)
![Jquery](https://img.shields.io/badge/-Jquery-0d1117?style=for-the-badge&logo=jquery&logoColor)
![AJAX](https://img.shields.io/badge/-AJAX-0d1117?style=for-the-badge&logo=ajax&logoColor)
![Bootstrap](https://img.shields.io/badge/-Bootstrap-0d1117?style=for-the-badge&logo=bootstrap&logoColor)

---

## APRESENTAÇÃO

Gravações e imagens do sistema funcionando.

### Capturas de Tela

![apresentacao-infomusica-gif](https://github.com/user-attachments/assets/b630729c-7d2e-404c-904d-b5da5f76515a)

---

**Página de Login**

![login-infomusica](https://github.com/user-attachments/assets/8c44dc75-ae2a-4b54-9959-1249ab82b7ab)

---

**Página do Inventário**

![inventario-infomusica](https://github.com/user-attachments/assets/a440c958-ae16-41fd-9664-4b0c18385109)

---

**Página de Postagens**

![postagens-infomusica](https://github.com/user-attachments/assets/bf084b9f-3ddb-45aa-985b-1cf123a3d33d)

---

**Página da Lista de Solicitações - Adminstrador**
![solicitacoes-adm-infomusica](https://github.com/user-attachments/assets/e738a707-b90e-4aa1-bf38-07de0ab8a5cf)

---

## INSTALAÇÃO

### Configurando o ambiente

 - Clone o [repositório](https://github.com/dvanael/infomusica/)

```bash
git clone https://github.com/dvanael/infomusica.git
```

- Crie um ambiente virtual

```bash
python -m venv .venv
```

- Ative o ambiente virtual

_windows_
```powershell
.venv/Scripts/activate
```

_linux, macOs_
```bash
source .venv/bin/activate
```

---

### Configurando sua máquina

- Instale as dependências

```bash
pip install -r requirements.txt
```

- Crie as variáveis de ambiente

```bash
python scripts/env_gen.py
```

> Se necessário, mude as configurações do  arquivo ``.env``

- Faça as migrações necessárias

```bash
python manage.py migrate
```

---

### Rodando o servidor

- Execute o arquivo scripts/setup.py para configuração inicial

```bash
python scripts/setup.py
```

> ⚠️ ATENÇÃO: Você receberá um usuário e senha para entrar no sistema.]

- Rode o sevirdor

```bash
python manage.py runserver
```

- Acesse a aplicação localmente

  - **[localhost:8000/](http://localhost:8000/)**

---
