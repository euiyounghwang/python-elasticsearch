#!/bin/bash

set -eu

SCRIPTDIR="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

docker run --rm --platform linux/amd64 -it -d \
  --name fn-elasticsearch-api-test --publish 8889:8889 --expose 8889 \
  --network bridge \
  -e ES_HOST=http://host.docker.internal:9209 \
  -v "$SCRIPTDIR:/app/FN-Basic-Services/" \
  fn-elasticsearch-api:test