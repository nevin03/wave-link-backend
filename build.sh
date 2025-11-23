#!/usr/bin/env bash
# exit on error
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# Create superuser if it doesn't exist
python manage.py shell -c "
from django.contrib.auth import get_user_model;
User = get_user_model();
import os;
username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin');
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com');
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'changeme123');
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password);
    print('Superuser created successfully')
else:
    print('Superuser already exists')
"
