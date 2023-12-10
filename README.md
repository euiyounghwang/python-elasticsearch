
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

