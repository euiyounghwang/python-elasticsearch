#!/bin/bash
set -e

SCRIPTDIR="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
# echo $SCRIPTDIR

cd $SCRIPTDIR
cd ..
filepath=`pwd`
# echo $filepath

source $filepath/.venv/bin/activate

# $filepath/.venv/bin/curator --config ./Curator/curator-config.yml --dry-run ./Curator/delete-indices.yml
curator --config ./Curator/curator-config.yml --dry-run ./Curator/delete-indices.yml