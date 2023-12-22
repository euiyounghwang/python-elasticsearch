
from opensearchpy import OpenSearch
from opensearchpy.helpers import bulk
import argparse
import warnings
import json

warnings.filterwarnings('ignore')


def get_headers():
    ''' Opensearch Header '''
    return {'Content-type': 'application/json', 'Connection': 'close'}

def get_es_instance(_host):
    # create a new instance of the Opensearch client class
    auth = ('admin', 'admin') # For testing only. Don't store credentials in code.
    ca_certs_path = '/full/path/to/root-ca.pem' # Provide a CA bundle if you use intermediate CAs with your root CA.
    # Optional client certificates if you don't want to use HTTP basic authentication.
    # client_cert_path = '/full/path/to/client.pem'
    # client_key_path = '/full/path/to/client-key.pem'

    # Create the client with SSL/TLS enabled, but hostname verification disabled.
    '''
    client = OpenSearch(
        hosts = [{'host': host, 'port': port}],
        http_compress = True, # enables gzip compression for request bodies
        http_auth = auth,
        # client_cert = client_cert_path,
        # client_key = client_key_path,
        use_ssl = True,
        verify_certs = True,
        ssl_assert_hostname = "localhost",
        ssl_show_warn = True,
        # ca_certs = ca_certs_path
    )
    '''
    # port = 9250
    es_client = OpenSearch(
        # hosts = [{'host': host, 'port': port}],
        hosts = _host,
        headers=get_headers(),
        http_auth = auth,
        use_ssl = True,
        verify_certs = False,
        timeout=600
    )   
    
    return es_client



if __name__ == "__main__":
    '''
    install : poetry add opensearch-py (opensearch-py = "^2.4.2")
    python tools/opensearch/opensearch_api.py
    '''
    parser = argparse.ArgumentParser(description="Index into Elasticsearch using this script")
    parser.add_argument('-e', '--es', dest='es', default="http://localhost:9250", help='host target')
    args = parser.parse_args()

    if args.es:
        host = args.es
    
    # --
    # Instance for the response time log
    client = get_es_instance(host)
    # --
    
    info = client.info()
    print(json.dumps(info, indent=2))
    # print(f"Welcome to {info['version']['distribution']} {info['version']['number']}!")

    index_name = 'python-test-index'
    index_body = {
        'settings': {
            'index': {
            'number_of_shards': 4
            }
        }
    }

    if client.indices.exists(index_name):
        client.indices.delete(index_name)
    response = client.indices.create(index_name, body=index_body)
    print('\nCreating index:')
    print(json.dumps(response, indent=2))
    
    '''
    actions = [
        {"_op_type": "index", "_index": "python-test-index", "_id": 1, "_source": {"field1": "value1"}}
    ]
    success, failed = bulk(client, actions)
    print(success, failed)
    '''
    actions = [
        {"index" : {"_index": index_name, "_id": 1}},
        {'title': 'Moneyball','director': 'Bennett Miller','year': '2011'},
         {"index" : {"_index": index_name, "_id": 2}},
        {'title': 'Moneyball','director': 'Bennett Miller','year': '2011'}
    ]
    response = client.bulk(body=actions)
    print(json.dumps(response, indent=2))
    
    q = 'miller'
    query = {
        'size': 5,
        # 'query': {
        #     'multi_match': {
        #     'query': q,
        #     'fields': ['*']
        #     }
        # }
        'query' : {
            'bool' : {
                'must' : [ 
                    {
                        'query_string' : {
                            'query': q,
                            'fields': ['*']
                        }
                    }
                ]
            }
        }
    }
    
    client.indices.refresh(index=index_name)
    
    response = client.search(
        body = query,
        index = index_name
    )

    print(json.dumps(response, indent=2))