# Projeto Brain AG

O Brain AG é um projeto de software que visa demonstrar via API o acesso

a base de dados Postgres, urilizando DRF(Django Rest Framework)

O projeto do banco de dados foi dividido em tres tabelas:

Produtor, Fazenda e Cultura sendo a partir  de produtor relaciomentos de N:N para 

fazenda e cultura

## Pré-requisitos para instalação:

Docker instalado

Python

Instalando o projeto:

Crie um ambiente virtual Python:

>python -m venv .venv

Ative o ambiente virtual:

>source .venv/bin/activate

```
Certifique-se de que o arquivo requirements.txt está na pasta raiz do projeto.
```


Instale as dependências do projeto:

> pip install -r requirements.txt

Verifique se o arquivo docker-compose.yml está na pasta raiz do projeto.

Inicie os containers Docker:

> docker-compose up -d

Aguarde a montagem dos containers.

Inicie o servidor Django:

insira o seguinte comando para criar um superuser:

> manage createsuperuser --username="admin"
 
 simplesmente informe o que o prompt pedir

 gere um token no painel de administração do admin e copi este token

 no authorization do Postman o Insominia pois o acesso as apis
 
 requer autenticação.


python manage.py runserver

>O servidor Django estará disponível em http://127.0.0.1:8000/.

Ferramentas para testar APIs:

Postman ou Insomnia

