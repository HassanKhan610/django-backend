# Task Manager API Setup Instructions
make an empty folder and open it in vscode or pycharm

## Local Setup

1. Clone the repository:

git clone https://github.com/HassanKhan610/django-backend.git

## Prerequisites
- Python 3.13.2
- pip 25.1.1
- virtualenv -> python -m venv .venv -> .venv/Scripts/activate
### OR use one from ctrl + shift + p and select create environment, then select venv and done it will activate itself

once your virtual env is setup
navigate to task_manager directory and then
run pip install -r requirements.txt

## after this simply run following
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# at the end run
python manage.py runserver

# I will share the postman/insomnia colletion for ease in api documentation

