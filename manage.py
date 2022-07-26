# django-admin startproject
# python manage.py startapp
# python manage.py startserver
# python manage.py makemigrations
# python manage.py migrate
# pip install django-tastypie 
# -- Getting ready for Deployment on Heroku
"""
Heroku
git --version
sudo snap install heroku --classic
heroku --version
pip install gunicorn
create Procfile file in main project directory not in app and write 
web: gunicorn 'projectname.wsgi' this wsgi file i spresent in the project named application folder as wsgi.py
"""
# python manage.py collectstatic this command move all the satic files of the admin app to static folder
# we have to "pip install whitenoise" specific for heroku n   http://whitenoise.evans.io/en/stable/
# right after the security middleware add "whitenoise.middleware.WhiteNoiseMiddleware"
"""
GIT REpository
cd directory to which is used to do version control
git init
git add . (every time you make changes)
if first_time:
    git config --global user.email "engr.mohsinq@gmail.com"
    git config --global user.name "MohsinQuddus"
else:
    git commit -m "Initial Commit"
heroku login    
automatic login using browser
heroku create 
or
heroku create "application name"
sudo apt-get update && sudo apt-get upgrade heroku
"""

#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Projects.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
