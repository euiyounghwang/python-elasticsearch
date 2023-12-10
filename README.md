
### Python-Elasticsearch

I will use this project as a basic api for building and searching with Elasticsearch 
- Build Docker for creating an index with sample metrics and searching with Elasticsearch
- Also run local environment with this project
- Build Docker Instance for testing with pytest

#### Install Poerty
```
https://python-poetry.org/docs/?ref=dylancastillo.co#installing-with-the-official-installer
```

#### Using Python Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate
```

#### Using Poetry: Create the virtual environment in the same directory as the project and install the dependencies with basic library:
```bash
poetry config virtualenvs.in-project true
poetry init
poetry add fastapi
poetry add uvicorn
poetry add pytz
poetry add elasticsearch==7.9.0
poetry add numpy
poetry add pytest
poetry add python-dotenv
```

#### Using Poetry Dependency for creating new environment
```bash
source .venv/bin/activate
poetry install
```

### Pytest
```bash
(.venv) ➜  python-elasticsearch git:(master) ./pytest.sh 
============================================= test session starts ==============================================
platform darwin -- Python 3.9.7, pytest-7.4.3, pluggy-1.3.0 -- /Users/euiyoung.hwang/ES/Python_Workspace/python-elasticsearch/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/euiyoung.hwang/ES/Python_Workspace/python-elasticsearch/tests
configfile: pytest.ini
plugins: cov-4.1.0, anyio-3.7.1
collected 7 items                                                                                              

tests/test_api.py::test_skip SKIPPED (no way of currently testing this)                                  [ 14%]
tests/test_api.py::test_api PASSED                                                                       [ 28%]
tests/test_api.py::test_CRUD_api PASSED                                                                  [ 42%]
tests/test_elasticsearch.py::test_elasticsearch PASSED                                                   [ 57%]
tests/test_elasticsearch.py::test_indics_analyzer_elasticsearch PASSED                                   [ 71%]
tests/test_elasticsearch.py::test_search_elasticsearch SKIPPED (no way of currently testing this)        [ 85%]
tests/test_elasticsearch.py::test_api_es_search SKIPPED (no way of currently testing this)               [100%]
```