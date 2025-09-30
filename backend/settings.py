# backend/settings.py
import os
from pathlib import Path
import environ

BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

# Core security
SECRET_KEY = env("SECRET_KEY")
DEBUG = env.bool("DEBUG", default=False)
ALLOWED_HOSTS = []

# DATABASES: supports DB_URL or individual vars
# Example DB_URL:
#   mysql://USER:PASSWORD@HOST:PORT/NAME
# django-environ will parse it and set ENGINE automatically.
if env("DB_URL", default=None):
    DATABASES = {
        "default": env.db("DB_URL")  # parses mysql://... string
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": env("DB_NAME"),
            "USER": env("DB_USER"),
            "PASSWORD": env("DB_PASSWORD"),
            "HOST": env("DB_HOST", default="localhost"),
            "PORT": env("DB_PORT", default="3306"),
        }
    }

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "api",  # your app
]

# (other usual Django settings…)
