# Petgram

_Pet social network_

## Starting 🚀

_These instructions will allow you to get a copy of the project running on your local machine for development and testing purposes._

Look **Deployment** to know how to deploy the project.


### Pre requirements 📋

_What things do you need to install the software and how to install them_

```
asgiref == 3.3.4
Django == 3.2
Almohada == 8.2.0
pytz == 2021.1
sqlparse == 0.4.1
```

### Installation 🔧

_A series of step-by-step examples that tells you what to run to get a development environment running_

_Clone the repository_

```
git clone git@github.com:luckdeluxe/Petgram.git / petgram.git &&  cd petgram
```

_Create a virtual Python environment:_

```
python3 -m venv .venv
```

_Activate the virtual environment_

```
sorce .venv/bin/activate
```

_Create database from models_

```
python3 manage.py makemigrations
python3 manage.py migrate
```

## Running the tests ⚙️

```
python3 manage.py runserver
```
