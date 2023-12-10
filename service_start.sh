#!/bin/bash
set -e

function get_value_from_yaml()
{
    #cat ./config.yaml | jq .app.es.es_host
    ES_HOST=$(cat ./config.yaml | jq .app.es.es_host)
    ES_HOST=$(sed -e 's/^"//' -e 's/"$//' <<< $ES_HOST)
    echo 'get_value_from_yaml -> ' ${ES_HOST}
}

get_value_from_yaml
export PYTHONDONTWRITEBYTECODE=1

# Activate virtualenv && run serivce
SCRIPTDIR="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
cd $SCRIPTDIR
source .venv/bin/activate

# --
# Wating for ES
./wait_for_es.sh $ES_HOST

uvicorn main:app --reload --host=0.0.0.0 --port=8888 --workers 4