# Django CSV Analysis

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them?


sudo apt update sudo apt install python3 python3-pip python3-venv


### Installing

A step by step series of examples that tell you how to get a development environment running.

1. Clone the repository:

git clone https://github.com/askanio8/django_csv_analysis.git cd django_csv_analysis/


2. Install the required packages:

cp .env.example .env nano .env

Change keys and addresses in .env
python3 -m venv myvenv source myvenv/bin/activate pip install django setuptools pandas matplotlib django-environ gunicorn


3. Configure Django:

nano /django_csv_analysis/settings.py

Set Debug=False in settings.py
python manage.py migrate python manage.py collectstatic --noinput


## Running the Server

### Using Gunicorn


gunicorn --workers 1 --bind 0.0.0.0:8000 django_csv_analysis.wsgi:application


### Without Gunicorn and without Nginx


sudo /home/ubuntu/django_csv_analysis/myvenv/bin/python manage.py runserver 0.0.0.0:80


### With Nginx and without Gunicorn


python manage.py runserver 0.0.0.0:8000


## Configuring Nginx

1. Install Nginx and start the service:

sudo apt install nginx sudo systemctl start nginx sudo systemctl enable nginx


2. Set up the Nginx configuration:

sudo cp django_csv_analysis.nginx.conf /etc/nginx/sites-available/django_csv_analysis sudo cp nginx.conf /etc/nginx/nginx.conf sudo ln -s /etc/nginx/sites-available/django_csv_analysis /etc/nginx/sites-enabled/ sudo nginx -t sudo systemctl restart nginx


## Authors

* askanio8

