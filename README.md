### Developing a RESTful API using Django REST Framework. The development of this application is exclusively for studying the involved technologies.

### Technologies used in the project:
  * Django 4.1
  * Python 3.10
  * Django REST Framework 3.14
  
### To run the project:
#### Steps to run the project locally

Create a Python virtual environment (venv, virtualenv, etc.):

    $ virtualenv -p python3 venv

Activate the virtual environment:

    $ source venv/bin/activate

Install necessary packages:

    $ pip install -r requirements.txt
    
   
### Configuration of the .env file:

For security reasons, sensitive variables, keys, and configurations are stored in a .env file at the root of the Django project. To do this, simply create a normal text file named .env at the same level as manage.py.

In the file, you can specify:

    DEBUG=True

    SECRET_KEY='your_secret_key'

The default value of `DEBUG` is `False` if not specified. 
If `DATABASE_URL` is not specified, the project will run using SQLite.
The only truly necessary configuration is the `SECRET_KEY`.

Generate your `SECRET_KEY` using:

    import secrets
    secrets.token_hex(24)

### After these configurations, execute:

    $ python manage.py makemigrations
######
    $ python manage.py migrate
######
    $ python manage.py test
######    
    $ python manage.py runserver
