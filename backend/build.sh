#!/usr/bin/env bash
# Render Web Service 빌드 스크립트 (rootDir: backend 기준 실행)

set -o errexit

pip install --upgrade pip
pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate
