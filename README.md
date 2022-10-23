# Projeto Api E-comerce

### Desenvolvimento de uma RESTful API utilizando Django REST Framework para gerenciar um E-comerce.


### Tecnologias utilizadas no projeto:
  * Django 4.1
  * Python 3.9
  * Django REST Framework 3.14
  
### Para executar o projeto:
#### Passos para executar o projeto localmente

Criar um ambiente virtual Python (venv, virtualenv, etc.):

    $ virtualenv -p python3 venv

Ativar a venv:

    $ source venv/bin/activate

Instalar pacotes necessários:

    $ pip install -r requirements.txt
    
   
### Configuração do arquivo .env:

Por questões de segurança, variáveis, chaves e configurações sensíveis ficam em um arquivo .env na raiz do projeto Django. Para isso, basta criar um arquivo de texto normal com o nome .env no mesmo nível que manage.py.

No arquivo você pode informar:

    DEBUG=True

    SECRET_KEY='sua_chave_secreta'

O default do `DEBUG` é `False` se não for informado. 
Se `DATABASE_URL` não for informado, o projeto rodará utilizando o SQLite.
A única configuração realmente necessária é a `SECRET_KEY`.

### Após essas configurações, execute:
 
    $ python manage.py makemigrations
######
    $ python manage.py migrate
######
    $ python manage.py test

######    
    $ python manage.py runserver

