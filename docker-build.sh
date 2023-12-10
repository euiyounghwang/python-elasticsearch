#!/bin/bash

set -eu

#docker build --no-cache \


docker build \
  -f "$(dirname "$0")/Dockerfile" \
  -t fn-elasticsearch-api:es \
  --target runtime \
  "$(dirname "$0")/."


# docker build \
#   -f "$(dirname "$0")/Dockerfile" \
#   -t fn-elasticsearch-search-api:test \
#   --target fta_runtime \
#   "$(dirname "$0")/."
