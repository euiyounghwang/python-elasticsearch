#!/bin/bash
set -e

export PYTHONDONTWRITEBYTECODE=1

# Activate virtualenv && run serivce
SCRIPTDIR="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

cd $SCRIPTDIR
source .venv/bin/activate
uvicorn main:app --reload --host=0.0.0.0 --port=8888 --workers 4