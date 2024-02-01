
from elasticsearch import Elasticsearch
from dotenv import load_dotenv
from injector import logger, es_client, global_settings
import json

load_dotenv()

    
def create_logger(message):
    response = es_client.index(index=global_settings.get_es_index(), body=json.loads(message))
    logger.info(response)
        