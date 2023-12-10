#!/bin/bash
set -e

# sleep 60 
source /app/poetry-venv/bin/activate
cd /app/FN-Basic-Services
# python -m py.test -v tests --disable-warnings
poetry run py.test -v tests --disable-warnings