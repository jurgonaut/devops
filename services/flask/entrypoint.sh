#!/bin/bash
set -euo pipefail

deploy_env=${DEPLOY_ENV:-"prod"}
gunicorn_port=${PORT:-5000}

if [ $deploy_env = "prod" ]; then
    echo "Running in prod mode"
    gunicorn --bind 0.0.0.0:${gunicorn_port} --chdir src app:app
elif [ $deploy_env = "debug" ]; then
    echo "Running in debug mode"
    python src/app.py
else
    echo "Invalide ${DEPLOY_ENV}, must be either 'prod' or 'debug'"
fi
