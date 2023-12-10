#!/bin/bash
set -e
source ./DevOps_Shell/read_config.sh

# --
# Call this function from './DevOps_Shell/read_config.yaml.sh' to get ES_HOST value in config.yaml file
get_value_from_yaml
# --

export PYTHONDONTWRITEBYTECODE=1

# Activate virtualenv && run serivce
SCRIPTDIR="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
cd $SCRIPTDIR
source .venv/bin/activate

# --
# Wating for ES
./wait_for_es.sh $ES_HOST

uvicorn main:app --reload --host=0.0.0.0 --port=8888 --workers 4