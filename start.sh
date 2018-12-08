#!/bin/bash

# Start Gunicorn processes
echo Collecting static files
python manage.py collectstatic --no-input
echo Starting Gunicorn.
exec gunicorn inetrecomgr.wsgi:application \
    --bind 0.0.0.0:8008 \
    --log-level=debug \
    #--access-logfile /var/log/gunicorn-access.log \
    #--error-logfile /var/log/gunicorn-error.log \
    --workers 3
