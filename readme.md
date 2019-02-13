# Development Setup

## Clone Project and Configure the Python Virtualenv:

### Create virtualenv and activate:

```
cd mcb

python3 -m venv venv
```

### Activate virtualenv:

```
source venv/bin/activate
```

### Install packages:

```
pip3 install --upgrade pip3

pip3 install -r requirements.txt
```


### create .env file by copyings the contents of .env.example

```
cp .env.example .env
```


### Database migration:
Create a database  in mysql/postgre and add a user with read/write permissions. Add the serrings to .env file

```
python3 manage.py migrate
```
### Create first User
Create super user:

```
python3 manage.py createsuperuser
```

Start the server:

```
python3 manage.py runserver
```

### Pre-populate database with data

```
python3 manage.py seed loan --number=15
```


### Running Tests
```
python3 manage.py test loan.tests
```

### Assumptions made.
Only the super user can login and view all users and loans. Other users can only login and view their loans. They can also apply for a loan.

I am using Django admin to manage all models. Thus i have registered them with the admin site. Atleat one admin is required

A user needs to register with full details to apply for a loan 