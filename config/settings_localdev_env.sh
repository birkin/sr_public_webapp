#!/bin/bash


## LOCALDEV settings for django `sr_public_webapp_project`
##
## This file is loaded by `env/bin/activate` when running locally...
## ...and by `project/config/passenger_wsgi.py` on our servers.
##
## When deploying on our servers, copy this file to the appropriate place, edit it, 
## ...and point to it from activate and the apache <Location> entry.


## ============================================================================
## standard project-level settings
## ============================================================================

export SR_PUBWEBAPP__SECRET_KEY="example_secret_key"

export SR_PUBWEBAPP__DEBUG_JSON="true"

export SR_PUBWEBAPP__ADMINS_JSON='
    [
      [
        "exampleFirst exampleLast",
        "example@domain.edu"
      ]
    ]
    '

export SR_PUBWEBAPP__ALLOWED_HOSTS_JSON='["127.0.0.1", "127.0.0.1:8000", "0.0.0.0:8000", "localhost:8000"]'  # must be json

# export SR_PUBWEBAPP__DATABASES_JSON='
#     {
#       "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "HOST": "",
#         "NAME": "../DB/sr_public_webapp_project.sqlite3",
#         "PASSWORD": "",
#         "PORT": "",
#         "USER": ""
#       }
#     }
#     '

export SR_PUBWEBAPP__STATIC_URL="/static/"
export SR_PUBWEBAPP__STATIC_ROOT="/static/"

export SR_PUBWEBAPP__EMAIL_HOST="localhost"
export SR_PUBWEBAPP__EMAIL_PORT="1026"  # will be converted to int in settings.py
export SR_PUBWEBAPP__SERVER_EMAIL="donotreply_x-project@domain.edu"

export SR_PUBWEBAPP__LOG_PATH="../logs/sr_public_webapp_project.log"
export SR_PUBWEBAPP__LOG_LEVEL="DEBUG"

export SR_PUBWEBAPP__CSRF_TRUSTED_ORIGINS_JSON='["localhost", "127.0.0.1"]'

## https://docs.djangoproject.com/en/3.2/topics/cache/
## - TIMEOUT is in seconds (0 means don't cache); CULL_FREQUENCY defaults to one-third
export SR_PUBWEBAPP__CACHES_JSON='
{
  "default": {
    "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
    "LOCATION": "../cache_dir",
    "TIMEOUT": 0,
    "OPTIONS": {
        "MAX_ENTRIES": 1000
    }
  }
}
'

## ============================================================================
## app
## ============================================================================

export SR_PUBWEBAPP__README_URL="https://github.com/birkin/sr_public_webapp_project/blob/main/README.md"

## end --------------------------------------------------------------
