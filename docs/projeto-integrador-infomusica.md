INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO RIO GRANDE DO NORTE

ELYABE BEZERRA DE MEDEIROS

JOÃO ANAEL BARBOSA SILVA

JOÃO PEDRO DA SILVA MOURA

WEVERTON ANTÔNIO DA SILVA CAMPOS

**INFOMUSICA - UM SISTEMA WEB PARA DIVULGAÇÃO E RESERVA DO LABORATÓRIO DE PRÁTICAS MUSICAIS DO CAMPUS IFRN SPP**

São Paulo do Potengi/RN

2023

---

**LISTA DE ILUSTRAÇÕES**

Imagem 1. Protótipo de tela da página Inicial.

Imagem 2. Protótipo de tela da página de Minhas Solicitações.

Imagem 3. Protótipo de tela da página de Criar Solicitações.

Imagem 4. Protótipo de frontend da página Minhas Solicitações feito em Django.

Imagem 5. Diagrama de casos de uso.

Imagem 6. Diagrama de Atividades.

Imagem 7. Diagrama de Classes do sistema.

Imagem 8. Modelo de banco de dados do sistema.

Imagem 9. Diagrama de sequência

Imagem 10. Modelo de alto nível de arquitetura do sistema.

---

<a name="_gjdgxs"></a>**LISTA DE QUADROS**

Quadro 1. Lista de requisitos funcionais do sistema.

Quadro 2. Lista de requisitos não funcionais do sistema

---

**LISTA DE SIGLAS**

|      |                                                                              |
| :--- | :--------------------------------------------------------------------------- |
| CMC  | _Content Management System_                                                  |
| CSRF | _Cross-site Request Forgery_                                                 |
| IFRN | _Instituto Federal de Educação, Ciência e Tecnologia do Rio Grande do Norte_ |
| MTV  | _Model, Template, View_                                                      |
| SPP  | _São Paulo do Potengi_                                                       |
| SUAP | _Sistema Unificado de Administração Pública_                                 |
| RF   | _Requisitos Funcionais_                                                      |
| RNF  | _Requisitos não Funcionais_                                                  |
| UML  | _Unified Modeling Language_                                                  |

---

<a name="_30j0zll"></a>**SUMÁRIO**

[**1 INTRODUÇÃO**](#_s6tmlwbzhiry)

[1.1 JUSTIFICATIVA](#_zfco8fbgf27r)

[1.2 ESCOPO](#_io6rh1r5inl3)

[1.3 PÚBLICO-ALVO](#_xp9t2b7ptnl6)

[1.4 OBJETIVOS](#_9dwi75lin8bz)

[**2 ANÁLISE E PROJETO**](#_1konar27bere)

[2.1 VISÃO GERAL DO SISTEMA](#_9jxng9j03rkp)

[2.2 ATORES DO SISTEMA](#_nngft1knahq9)

[2.3 LEVANTAMENTO DE REQUISITOS](#_qu4giov7pszp)

[2.3.1 Técnicas Utilizadas](#_xmsl5v39pesk)

[2.3.2 Requisitos Funcionais](#_4vd2jj4b52ed)

[2.3.3 Requisitos Não Funcionais](#_jj740vsd1lgx)

[2.4 DIAGRAMAS DE CASOS DE USO](#_qr3h7a33e5uo)

[2.5 EXPANSÃO DO CASOS DE USO](#_2rj7li5e8dw)

[2.6 DIAGRAMA DE ATIVIDADES](#_vc0nrxcv8krq)

[2.7 DIAGRAMA DE CLASSES](#_wjeavhqntvdc)

[2.8 MODELO DE DADOS](#_6ps876s0x264)

[2.9 DIAGRAMA DE SEQUÊNCIA](#_ohm2mfeqn3mw)

[2.10 MODELO DE ALTO NÍVEL DE ARQUITETURA](#_py712yyepoff)

[**3 PRINCIPAIS DESAFIOS ATÉ O MOMENTO 21**](#_fe13qiw77e6a)

[3.1 ETAPA 1](#_wblfkwirprym)

[3.2 ETAPA 2](#_8aws6417hj89)

[3.3 ETAPA 3](#_xv6m12u0yo3f)

[3.4 ETAPA 4](#_kfokq67gbmbb)

[**4 RESULTADOS**](#_12h52cw21nkc)

[**5 CONCLUSÃO**](#_el9vw1mlkvzf)

[**REFERÊNCIAS**](#_61h06xmsoetx)

---

<a name="_1fob9te"></a>

# <a name="_s6tmlwbzhiry"></a>**INTRODUÇÃO**

Sabemos que é importante ter um espaço para suas atividades acadêmicas, como eventos e reuniões, com acessibilidade adequada. Com o objetivo de oferecer uma maneira eficiente e organizada para reservar a sala de música e difundir a cultura musical, desenvolvemos esse sistema que visa simplificar o processo de agendamento e divulgar eventos relacionados ao universo musical.

A plataforma foi desenvolvida para atender as necessidades da comunidade acadêmica do campus IFRN SPP, proporcionando uma experiência fácil de usar e flexível. Sendo possível reservar a sala de forma conveniente, evitando conflitos de horário e garantindo o espaço necessário para a sua atividade, além de ter acesso a mais informação através dos posts e do inventário de instrumentos.

## <a name="_zfco8fbgf27r"></a>JUSTIFICATIVA

A situação sobre o controle de fluxo da sala de música do Campus IFRN SPP é informal. Geralmente, todo o controle é gerenciado por Priscila Gomes, a professora de música, sendo necessário entrar em contato com ela, pessoalmente ou via e-mail, para reservar o uso monitorado do laboratório. É necessário o preenchimento de um formulário de forma manual, informando quando e como o laboratório será utilizado.

Diante desse problema, é proposto o desenvolvimento de um sistema web para a automatização desse processo, tendo em vista as necessidades apresentadas pelos usuários. É sobre agilizar o processo e evitar conflitos de horário, e até por isso o sistema contará com uma tabela de horários reservados e disponíveis.

A respeito do sistema de posts, acreditamos que o Instagram e o SUAP, os atuais meios de divulgação dos eventos, possuem muita informação e a maioria não se refere ao mundo da música. Portanto, seria interessante o criarmos.

Quanto ao inventário: é uma página onde há fotos, sons e classificações de instrumentos musicais, até daqueles que o campus ainda não adquiriu. Temos a intenção de ajudar no aprendizado dos alunos e aumentar o interesse deles.

## <a name="_io6rh1r5inl3"></a>ESCOPO

O objetivo desse projeto é desenvolver e implementar um sistema web no Campus IFRN SPP, a fim de facilitar o acesso da sala de música aos alunos, melhorar o controle de fluxo da sala de música para aulas, projetos e ensaios, e difundir a cultura musical através de postagens e do inventário de instrumentos.

Esse sistema deve ser capaz de receber as solicitações dos alunos para a reserva do laboratório de prática musicais, gerenciar essas solicitações, permitir comunicação entre aluno e professor, notificar os usuários sobre eventos, aulas e suas solicitações, e contar com o sistema de inventário.

O projeto será concluído quando todos os requisitos forem devidamente testados e implementados corretamente.

## <a name="_xp9t2b7ptnl6"></a>PÚBLICO-ALVO

O sistema será utilizado pelo principal público-alvo:

**Alunos:** Eles serão os principais usuários do sistema, podendo fazer solicitações de reserva e ter um contato virtual com os professores.

**Professores:** Os professores e servidores responsáveis pelo laboratório de música, poderão gerenciar as solicitações, requisitar bolsistas para e dar prioridade para aulas e projetos que acontecerão no laboratório.

## <a name="_9dwi75lin8bz"></a>OBJETIVOS

O sistema visa facilitar o processo de reserva e administração das atividades realizadas no laboratório de música e difundir a cultura musical. Tendo como função principal a organização e controle do fluxo de atividades, permitindo gerenciamento e solicitações de reservas.

# <a name="_1konar27bere"></a>**ANÁLISE E PROJETO**

## <a name="_9jxng9j03rkp"></a>VISÃO GERAL DO SISTEMA

`	`Esse sistema web permitirá aos usuários acesso a informações sobre a sala de música, como projetos, aulas, e instrumentos, fazer solicitações para ensaios, gravações, elaboração de projetos e entre outros. Sendo divido em três módulos, descritos a seguir:

- **Módulo Público:** é utilizado pelos usuários que não são registrados no sistema, chamados aqui de usuários avulsos, podendo visualizar projetos, eventos, e o inventário, cadastrar-se no sistema, efetuar login e recuperar senha.
- **Módulo Aluno:** é utilizado por usuários que são registrados no sistema com acesso de aluno, estendendo os usuários públicos, podendo editar seu perfil, fazer solicitações para o uso monitorado do laboratório, visualizar projetos, eventos, o inventário, se inscrever para projetos e solicitar
- **Módulo Professor:** é utilizado por usuários que são registrados no sistema com acesso de administrador. Estendendo os usuários que são alunos, podendo gerenciar projetos, eventos, solicitações no sistema e o inventário.

## <a name="_nngft1knahq9"></a>ATORES DO SISTEMA

Ao total o sistema possui 3 atores, conforme descrito abaixo:

- **Avulso:** diz respeito aos usuários sem registro no sistema. Podem visualizar os projetos e eventos, inventário e se cadastrar no sistema.
- **Aluno:** diz respeito aos usuários com registro no sistema e acesso de aluno. Eles podem acessar o sistema, fazer solicitações de reserva, ter acesso às informações dos projetos que estão inscritos e solicitar acesso de administrador.
- **Administrador:** diz respeito aos usuários com registro e acesso de professor no sistema. Podem gerenciar as solicitações feitas por alunos, os projetos, os posts e o inventário.

## <a name="_qu4giov7pszp"></a>LEVANTAMENTO DE REQUISITOS

### <a name="_xmsl5v39pesk"></a>**Técnicas Utilizadas**

**Observação:** O levantamento de requisitos foi realizado incorporando o papel do usuário e observando a problemática, discutindo com a equipe e formulando um consenso geral sobre os requisitos.

**Brainstorm:** Discussões com a equipe foram feitas com a proposta de reunir o maior número possível de ideais e identificação de requisitos, com base nos problemas apresentados.

**Prototipagem:** Diante das ideias propostas pela equipe, foi esboçado e elaborado protótipos de tela no Canvas e a programação de um protótipo em Django, focando na validação dos requisitos de Solicitações e seus Casos de Uso, conforme nas imagens a seguir.

| Imagem 1. Protótipo de tela da página Inicial. |
| :--------------------------------------------: |
|     ![](img/prototipo-de-tela-inicial.png)     |

Fonte: Elaboração própria (2023).

|  Imagem 2. Protótipo de tela da página Minhas Solicitações.  |
| :----------------------------------------------------------: |
| ![](img/prototipo-de-tela-da-pagina-minhas-solicitacoes.png) |

Fonte: Elaboração própria (2023).

| <p></p><p></p><p></p><p>Imagem 3. Protótipo de tela da página de Criar Solicitações.</p> |
| :--------------------------------------------------------------------------------------: |
|                ![](img/prototipo-de-tela-da-pagina-criar-solicitacao.png)                |

Fonte: Elaboração própria (2023).

### <a name="_4vd2jj4b52ed"></a>**Requisitos Funcionais**

Os requisitos funcionais representam as principais funcionalidades que o sistema deve efetuar. Eles são representados pelo Quadro 1.

<a name="_2s8eyo1"></a>Quadro 1. Lista de requisitos funcionais do sistema.
| | | | |
| :-------------------------------------------------------------------------: | :----------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------ |
| **Código** | **Nome** | **Descrição** | **Categoria** |
| RF001 | <p>Realizar cadastro no sistema</p><p></p> | O sistema deve permitir aos usuários realizar cadastro no sistema informando seu nome, sobrenome, email e senha de registro. | `   `_Alta_ |
| RF002 | Realizar login | O sistema deve permitir aos usuários realizar login para acesso a área restrita do sistema. O usuário deverá informar seu e-mail e senha de registro para realizar seu login. | `   `_Alta_ |
| <p>RF003 </p><p></p> | Recuperar senha | O sistema deve permitir aos usuários que eles recuperem sua senha informando o e-mail de cadastro. | `  `_Média_ |
| <p>RF004 </p><p></p> | Editar perfil | O sistema deve permitir aos usuários cadastrados modificar as informações de seu perfil de cadastro. Ao clicar em “Meu Perfil” é mostrado ao usuário nome, matrícula, e-mail, um botão para abrir um formulário para editar perfil. | `  `_Média_ |
| RF005 | Visualizar Calendário | O sistema deve permitir aos usuários acesso a um calendário onde serão exibidos os horários livres e ocupados do mês. | `  `_Média_ |
| <p>RF006</p><p></p> | Realizar Solicitação de Reserva | O sistema deve permitir aos usuários cadastrados realizar solicitação para reservar a sala de música. Ao clicar na opção “Fazer Solicitação” é exibido ao usuário um formulário para preenchimento das informações necessárias como data da reserva, horários de entrada e saída, um campo de texto para justificar o uso da sala e um botão enviar. | `   `_Alta_ |
| <p>RF007</p><p></p> | Listar Solicitações | O sistema deve permitir aos usuários cadastrados visualizar suas solicitações enviadas ao clicar na opção “Minhas Solicitações" no menu principal. Ao clicar nessa opção, é exibido ao usuário uma lista de suas solicitações com uma prévia, a opção de editar e excluir a solicitação. | `   `_Alta_ |
| RF008 | Editar Solicitação | O sistema deve permitir aos usuários editar as informações preenchidas das solicitações enviadas ao clicar na opção “Editar” na solicitação que deseja modificar. | `  `_Média_ |
| <p>RF009</p><p></p> | Excluir Solicitação | O sistema deve permitir aos usuários excluir as solicitações enviadas ao clicar na opção “Excluir” na solicitação que deseja deletar. | `  `_Média_ |
| RF010 | Promover Usuário | O sistema deve permitir aos usuários administradores do sistema promover usuários alunos. Ao clicar no botão “Permissão”, o administrador pode mudar o grupo do usuário aluno para administrador. | `  `_Baixa_ |
| <p>RF011</p><p></p> | Gerenciar Solicitações | O sistema deve permitir aos administradores poderem aceitar ou negar as solicitações enviadas pelos alunos. Caso negado, uma justificativa pode ser enviada. | `   `_Alta_ |
| RF012 | Detalhar Solicitação no Calendário | O sistema deve permitir aos usuários detalhar as informações de uma solicitação registrada no sistema. Ao clicar na solicitação presente no calendário, é exibido ao usuário quem fez a solicitação, data, horários da reserva e justificativa de uso da sala. | `   `_Alta_ |
| RF013 | Justificar Solicitação | O sistema deve permitir aos administradores aceitar ou negar as solicitações enviadas. É exibido ao administrador um campo de texto para justificar o porquê de aprovada ou negada. | `  `_Média_ |
| RF014 | Criar nova postagem | O sistema deve permitir aos administradores a criação de postagens de diversos tipos. | `  `_Média_ |
| RF015 | Editar postagem | O sistema deve permitir aos administradores editarem as próprias postagens. | `   `_Média_ |
| RF016 | Excluir postagem | O sistema deve permitir aos administradores excluírem as próprias postagens. | `    `_Média_ |
| RF017 | Adicionar instrumento ao inventário | O sistema deve permitir aos administradores adicionar uma imagem, um arquivo de áudio e informações de classificação sobre algum instrumento. | `   `_Média_ |
| RF018 | Editar instrumento | O sistema deve permitir aos administradores a edição das informações e mídias sobre cada instrumento. | `   `_Média_ |
| RF019 | Excluir instrumento | O sistema deve permitir aos administradores a exclusão de algum instrumento. | `   `_Baixa_ |
| RF020 | Notificações de Solicitações | O sistema deve enviar email para notificar novas solicitações registradas no sistema. Um email é enviado para os usuários administradores quando uma nova solicitação é registrada. Após ter seu status registrado pelo administrador, um email notificando se a solicitação foi aprovada, ou não, é enviada para o usuário que a criou. | _Alta_ |

Fonte: Elaboração própria (2023).

### <a name="_jj740vsd1lgx"></a>**Requisitos Não Funcionais**

Os requisitos não funcionais estão relacionados às restrições do sistema quanto a sua disponibilidade, desempenho e segurança. Eles são representados pelo Quadro 2, mostrado a seguir.

<a name="_3rdcrjn"></a>Quadro 2. Lista de requisitos não funcionais do sistema

|                      Cód.                       |                                                                                                        Descrição                                                                                                        | Categoria |
| :---------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-------: |
|         <p>RNF001 </p><p>Paginação</p>          |                                                   O sistema deve limitar a quantidade de solicitações visualizados por paginação de até sete solicitações por página.                                                   |  Produto  |
|      <p>RNF002 </p><p>Acesso Restrito</p>       | O sistema não deverá permitir o acesso de usuários não cadastrados a área restrita do sistema. As funcionalidades do sistema serão dispostas conforme os seguintes níveis de permissão: público, alunos, administrador. |  Produto  |
|          RNF003 Criptografia de senha           |                                                                    O sistema deverá criptografar a senha de usuário através do CSRF Token do Django.                                                                    |  Produto  |
|       <p>RNF004</p><p>Disponibilidade</p>       |                                                       O portal de conteúdos do sistema deverá estar disponível aos usuários 24 horas por dia e 7 dias por semana.                                                       |  Produto  |
|   <p>RNF005</p><p>Responsividade</p><p> </p>    |                                                         O site do sistema deverá estar responsivo, de modo que se torne de fácil acesso em diversos aparelhos.                                                          |  Produto  |
| <p>RNF006</p><p>Duplicidade de solicitações</p> |                                                                           O sistema deverá impedir que o usuário crie solicitações idênticas.                                                                           |  Produto  |
|   <p>RNF007</p><p>Limitação de caracteres</p>   |                                                                               O sistema deve limitar as justificativas a 250 caracteres.                                                                                |  Produto  |

Fonte: Elaboração própria (2023).

## <a name="_qr3h7a33e5uo"></a>DIAGRAMAS DE CASOS DE USO

Neste projeto, está sendo empregada a UML, uma linguagem de modelagem que aborda os princípios essenciais da programação orientada a objetos. A UML é usada para representar, de maneira clara e precisa, sistemas computacionais que seguem o modelo de orientação a objetos (SILVA, 2008).

O diagrama de casos de uso é utilizado para o levantamento de requisitos, atores do sistema e como eles interagem entre si, além de facilitar a comunicação do analista com o cliente.

Deste modo, considerando os requisitos funcionais e atores desse projeto, foram definidos dez casos de uso, conforme ilustrado na Imagem 5.

Imagem 5. Diagrama de casos de uso.

![](img/diagrama-de-casos-de-uso.png)

Fonte: Elaboração própria (2023).

Apenas um caso de uso foi considerado como de maior risco. Sendo este: Gerenciar Minhas Solicitações.

## <a name="_2rj7li5e8dw"></a>EXPANSÃO DO CASOS DE USO - GERENCIAR MINHAS SOLICITAÇÕES

O caso de uso Gerenciar Minhas Solicitações é o caso de maior risco desse sistema. Nessa seção são especificadas as ações que um usuário deve realizar no sistema com objetivo de criar uma solicitação no sistema. Usuários alunos e administradores podem criar solicitações.

**Atores**

Aluno, Administrador

**Pré-condição**

O usuário deve estar logado no sistema e estar em “Minhas Solicitações”

**Pós-condição**

O sistema exibe as solicitações do usuário.

**Requisitos funcionais:**

RF006 - Realizar Solicitação

RF007 - Listar Solicitações

RF008 - Editar Solicitação

RF009 - Excluir Solicitação

**Requisitos não funcionais**

RNF001 - Paginação

RNF002 - Acesso Restrito

RNF006 - Duplicidade de solicitações

**Fluxos Principal**

1. Na tela de minhas solicitações, o usuário clica em “Criar solicitação”.

1. Sistema apresenta o formulário de criação de solicitações.
1. O usuário envia a solicitação com participantes, horários, equipamento e justificativa.
   1. Solicitação já criada.
1. O sistema adiciona a solicitação à lista de solicitações do usuário e exibe todas as suas solicitações enviadas.
1. O sistema exibe a solicitação e a envia para aprovação dos administradores.

**Fluxos Alternativos**

1a. Usuário quer editar uma solicitação enviada.

1. O usuário seleciona a solicitação e clica em “Editar”.
1. O sistema carrega as informações da solicitação.
1. O usuário informa os dados que serão alterados.
1. O usuário confirma as alterações.
1. O sistema reenvia a solicitação para aprovação dos administradores.

1b. Usuário quer excluir uma solicitação enviada.

1. O usuário seleciona a solicitação e clica em “Excluir”.
1. O sistema exclui todos os dados do banco referente ao curso.

4a. Campo obrigatório não foi preenchido.

1. O sistema informa que os campos obrigatórios devem ser preenchidos.

4b. Duplicidade de dados.

1. O sistema informa que o usuário enviou uma solicitação com os mesmos dados.

## <a name="_vc0nrxcv8krq"></a>DIAGRAMA DE ATIVIDADES

**Gerenciar Minhas Solicitações**

Imagem 6. Diagrama de Atividades

![](img/diagrama-de-atividades.png)

Fonte: Elaboração própria (2023)

## <a name="_wjeavhqntvdc"></a>DIAGRAMA DE CLASSES

Imagem 7. Diagrama de Classes do sistema

![](Aspose.Words.b311b1a0-0a2d-4b79-9d5c-87604b9963d7.006.png)

Fonte: Elaboração própria (2023)

## <a name="_6ps876s0x264"></a>MODELO DE DADOS

**Modelo Físico**

Imagem 8. Modelo de banco de dados do sistema.

![](img/modelo-fisico-do-banco-de-dados-do-sistema.png)

Fonte: Elaboração própria (2023).

##

## <a name="_tqhmuzgf6rnw"></a><a name="_ohm2mfeqn3mw"></a>DIAGRAMA DE SEQUÊNCIA

Imagem 9. Diagrama de sequência

![](img/diagrama-de-sequencia.png)

Fonte: Elaboração própria (2024)

##

## <a name="_lmyiopbk4wvu"></a><a name="_py712yyepoff"></a>MODELO DE ALTO NÍVEL DE ARQUITETURA

Imagem 10. Modelo de alto nível de arquitetura do sistema em MTV.

![](img/modelo-de-arquitetura-mtv.png)

Fonte: Elaboração própria (2024)

# <a name="_fe13qiw77e6a"></a>**PRINCIPAIS DESAFIOS ATÉ O MOMENTO**

## <a name="_wblfkwirprym"></a>ETAPA 1

Uma das dificuldades iniciais foi a formação da equipe, visto que inicialmente Anael e Elyabe estavam sozinhos. Também, Weverton e João Pedro estavam com um tema semelhante ao tema de Anael. Logo após essa falta de comunicação, a equipe foi formada “em cima da hora”, o que levou a um planejamento às pressas do que foi cobrado na Etapa 1.

Levantamento de RNF, já que os apresentados até agora são genéricos e pouco elaborados.

## <a name="_8aws6417hj89"></a>ETAPA 2

Dentre as dificuldades enfrentadas durante essa etapa, uma delas foi a decisão do que realmente iríamos fazer nesse projeto. Um blog? Um site para reservas? Por muito tempo se manteve essa dúvida e dificuldade de alinhamentos de ideias entre nós e a nossa co-orientadora Priscila. No fim, isso se resolveu e continuamos com o sistema de reservas, mas provavelmente iremos criar um CMS e juntar com o sistema de reservas em algum momento.

A elaboração e entendimento da expansão de casos de uso também foi uma dificuldade, juntamente com a programação do projeto em Django.

## <a name="_xv6m12u0yo3f"></a>ETAPA 3

Muitas programação e pouco documento, mas estamos no caminho. Nosso

orientador, Diego Cirilo, aprovou o funcionamento do CRUD e agora estamos marcando reuniões para elaboração e implementação das propostas da nossa co-orientadora, Priscila.

E também vamos alinhar o esse documento com o projeto em Django.

## <a name="_kfokq67gbmbb"></a>ETAPA 4

Tivemos poucos problemas relevantes aqui, o que tentamos fazer nós conseguimos. O único detalhe ruim dessa etapa foi o fato de que não conseguimos marcar reuniões.

# <a name="_12h52cw21nkc"></a>**RESULTADOS**

Todos nós gostamos do resultado final, não existe algo em específico que tenha faltado no nosso projeto, embora nós tenhamos tido alguns problemas, sendo os principais deles a falta de organização para gerir o tempo e a falta de comunicação em alguns casos.

Acreditamos que conseguimos facilitar o processo de reserva e administração das atividades realizadas no laboratório de música e tornar a cultura musical mais forte, pois agora o uso pode ser agendado remotamente, com bons estímulos visuais e com o acesso dos usuários a vários posts informativos.

Esperamos que possa seguir como TCC no futuro e que cumpra seu propósito de ser utilizado pelo o IFRN e ter impacto cultural. O site já se encontra hospedado, podendo ser utilizado e conferido em nokixty.pythonanywhere.com

# <a name="_el9vw1mlkvzf"></a>**CONCLUSÃO**

O projeto foi muito agregador para nós, tanto pela parte acadêmica quanto pela parte pessoal. Nós ganhamos experiência real no desenvolvimento de um produto completo e totalmente funcional, trabalhando em equipe, fortalecendo nossos laços de amizade e aprendendo como lidar com opiniões diferentes.

O grande problema que enfrentamos e vamos tentar evitar ao máximo no futuro, deste projeto e de outros, é a dificuldade que tivemos em gerir o tempo, o que implicou em trabalho em cima da hora, e em estabelecer uma comunicação contínua, no sentido de que nem sempre todo mundo sabia de tudo. Na segunda etapa, por exemplo, ocorreu que Weverton e Elyabe desenharam algumas telas que, na verdade, já haviam sido feitas.

No mais, estamos orgulhosos e esperamos que o Infomusica marque o campus SPP, e que fique para sempre como nosso legado.

# <a name="_61h06xmsoetx"></a>**REFERÊNCIAS**

SILVA, Raimundo N. Sistudio 1.0: Sistema de controle de estúdio de áudio. 2008. Disponível em: <https://repositorio.uniceub.br/jspui/handle/235/4464>
