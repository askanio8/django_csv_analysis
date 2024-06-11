# Django CSV Analysis Setup Guide

Follow these steps to set up Django CSV Analysis on your server.

### Clone Repository

Clone the repository with the necessary branch:

```bash
git clone -b forawsec2 https://github.com/askanio8/django_csv_analysis.git
cd django_csv_analysis/
```

### Install Dependencies

Install Python and necessary packages:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### Configure Environment Variables
Copy the example environment file and edit it:

```bash
cp .env.example .env
nano .env
# Update keys and addresses in .env as needed
```

### Set Up Virtual Environment
Create and activate a Python virtual environment:

```bash
python3 -m venv myvenv
source myvenv/bin/activate
```

### Install Django and Other Packages
Install Django and required packages:

```bash
pip install django setuptools pandas matplotlib django-environ gunicorn
```

### Configure Django Settings
Edit Django settings to set Debug=False:

```bash
nano django_csv_analysis/settings.py
# Change DEBUG=False in settings.py
```

### Database Migration
Apply database migrations:

```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

# Run
If using Gunicorn for production:

```bash
gunicorn --workers 1 --bind 0.0.0.0:8000 django_csv_analysis.wsgi:application
```

For development or without Gunicorn:
```bash
sudo /home/ubuntu/django_csv_analysis/myvenv/bin/python manage.py runserver 0.0.0.0:80
```

For development with nginx and without Gunicorn:
```bash
python manage.py runserver 0.0.0.0:8000
```

### Install and Configure Nginx
Install Nginx and configure site:

```bash
sudo apt install nginx
sudo systemctl start nginx
sudo systemctl enable nginx

# Configure Nginx site
sudo cp django_csv_analysis.nginx.conf /etc/nginx/sites-available/django_csv_analysis
sudo nano /etc/nginx/sites-available/django_csv_analysis
# Update keys and addresses in django_csv_analysis

# Link site configuration
sudo ln -s /etc/nginx/sites-available/django_csv_analysis /etc/nginx/sites-enabled/

# Test Nginx configuration and restart
sudo nginx -t
sudo systemctl restart nginx
```

### Set Up HTTPS with Certbot
Install Certbot and configure HTTPS:

```bash
sudo apt install certbot python3-certbot-nginx

# Obtain SSL certificate
sudo certbot --nginx -d example.com

# Update /etc/nginx/sites-available/django_csv_analysis for HTTPS

# Test Nginx configuration and restart
sudo nginx -t
sudo systemctl restart nginx
```