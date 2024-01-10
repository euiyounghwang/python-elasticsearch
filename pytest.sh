#!/bin/bash
set -e

# Activate virtualenv && run serivce

# cd /Users/euiyoung.hwang/ES/Python_Workspace/python-django
SCRIPTDIR="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

cd $SCRIPTDIR
source .venv/bin/activate

# py.test -v tests
# poetry run py.test -v --junitxml=test-reports/junit/pytest.xml --cov-report html --cov tests/
poetry run py.test -v --cov tests/