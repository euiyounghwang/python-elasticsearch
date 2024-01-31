
from config.log_config import create_log
from config import config
from service.handler.es_search_handler import (SearchOmniHandler)
from service.handler.cluster_sharding import (ClusterShardingHandler)
from service.handler.es_query_builder import (QueryBuilder)
from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import yaml
import json
import os
from logger_logstash.logstash_logger import UDP_SOCKET

def read_config_yaml():
    with open('./config.yaml', 'r') as f:
        doc = yaml.load(f, Loader=yaml.FullLoader)
        
    logger.info(json.dumps(doc, indent=2))
    
    return doc

def get_headers():
    ''' Elasticsearch Header '''
    return {'Content-type': 'application/json', 'Connection': 'close'}


load_dotenv()
    
# Initialize & Inject with only one instance
logger = create_log()
doc = read_config_yaml()
# print(doc)

# Read_Doc with arguments from Docker -e option
"""
hosts = os.getenv("ES_HOST", doc['app']['es']['omni_es_host'])
"""
global_settings = config.Settings(logger, doc)



es_client = Elasticsearch(hosts=global_settings.get_Hosts(),
                          headers=get_headers(),
                          verify_certs=False,
                          timeout=600
)

SearchOmniHandlerInject = SearchOmniHandler(es_client, logger, doc['app'])
QueryBuilderInject = QueryBuilder(es_client, logger, doc['app'])
ClusterShardingInject = ClusterShardingHandler(es_client, logger)

# --
# logger logstash - to - elasticsearch
UDP_SOC = UDP_SOCKET("127.0.0.1", 5959)


