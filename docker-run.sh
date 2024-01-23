#!/bin/bash

set -eu

SCRIPTDIR="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

docker run --rm --platform linux/amd64 -it -d \
  --name fn-elasticsearch-api --publish 8888:8888 --expose 8888 \
  --network bridge \
  -e ES_HOST=http://host.docker.internal:9209 \
  -e KAFKA_HOST=host.docker.internal:29092,host.docker.internal:39092 \
  -e KAFKA_TOPIC=test-topic \
  -v "$SCRIPTDIR:/app/FN-Basic-Services/" \
  fn-elasticsearch-api:es


