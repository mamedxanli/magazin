#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn inetrecomgr.wsgi:application \
    --bind 0.0.0.0:8008 \
    --workers 3