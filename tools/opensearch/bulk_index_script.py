import json

import pandas as pd
from opensearchpy import OpenSearch
import argparse
import os
import warnings

warnings.filterwarnings('ignore')

# logger = log.reate_log()
MAX_BYTES = 1048576


def get_headers():
    ''' Elasticsearch Header '''
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


def create_index(es_client, _index):
    print(es_client)
    mapping = {
        "mappings": {
            "properties": {
                "title": {
                    "type": "text",
                    "analyzer": "english",
                    "fields": {
                        "keyword": {
                            "type": "keyword"
                        }
                    }
                },
                "ethnicity": 
                {
                    "type": "text",
                    "analyzer": "standard"
                },
                "director": 
                {
                    "type": "text",
                    "analyzer": "standard",
                    "fields": {
                        "keyword": {
                            "type": "keyword"
                        }
                    }
                },
                "cast": 
                {
                    "type": "text",
                    "analyzer": "standard",
                    "fields": {
                        "keyword": {
                            "type": "keyword"
                        }
                    }
                },
                "genre": 
                 {
                    "type": "text",
                    "analyzer": "standard",
                    "fields": {
                        "keyword": {
                            "type": "keyword"
                        }
                    }
                },
                "plot": 
                {
                    "type": "text",
                    "term_vector": "with_positions_offsets",
                    "analyzer": "standard",
                    "similarity": "BM25"
                },
                "year": {
                    "type": "integer"
                },
                "wiki_page": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword"
                        }
                    }
                }
            }
        }
    }

    try:
        if es_client.indices.exists(index=_index):
            es_client.indices.delete(index=_index, ignore=[400, 404])
            print("Successfully deleted: {}".format(_index))

        print('Creating..')
        # now create a new index
        es_client.indices.create(index=_index, body=mapping)
        es_client.indices.put_alias(_index, "omnisearch_search")
        es_client.indices.refresh(index=_index)
        print("Successfully created: {}".format(_index))
    except Exception as error:
        print('Error: {}, index: {}'.format(error, _index))


def Get_Buffer_Length(docs):
    """
    :param docs:
    :return:
    """
    max_len = 0
    for doc in docs:
        max_len += len(str(doc))

    return max_len


def load():
    from os.path import dirname
    df = (
        # pd.read_csv(dirname(__file__) + "/dataset/wiki_movie_plots_deduped.csv")
        pd.read_csv(os.path.join(os.path.dirname(__file__), "../dataset/wiki_movie_plots_deduped.csv"))
        .dropna()
        .sample(5000, random_state=42)
        .reset_index()
    )
    return df
    

def search(es, _index):
    response = es.search(
        index=_index,
        body={
                "query" : {
                    "bool": {
                        "must": [
                            {
                            "match_phrase": {
                                "cast": "jack nicholson",
                            }
                        }],
                        "filter": {"bool": {"must_not": {"match_phrase": {"director": "roman polanski"}}}}
                    }
                }
        }
    )

    # Show total counts from elasticsearch
    print("Total counts for search - {}".format(json.dumps(response['hits']['total']['value'], indent=2)))
    # Show first rows from elasticsearch
    print("response for search - {}".format(json.dumps(response['hits']['hits'][0], indent=2)))


def sinngle_indexing_mode_run(es, _index):
    print("sinngle_indexing_mode_run Loading..")
    df = load()
    print(df.loc[0])

    for i, row in df.iterrows():
        doc = {
            "title": row["Title"],
            "ethnicity": row["Origin/Ethnicity"],
            "director": row["Director"],
            "cast": row["Cast"],
            "genre": row["Genre"],
            "plot": row["Plot"],
            "year": row["Release Year"],
            "wiki_page": row["Wiki Page"]
        }

        es.index(index=_index, id=i, body=doc)


def buffer_indexing_mode_run(es, _index):
    print("buffer_indexing_mode_run Loading..")
    df = load()
    print(df.loc[0])
    
    actions = []
    for i, row in df.iterrows():
        doc = {
            "title": row["Title"],
            "ethnicity": row["Origin/Ethnicity"],
            "director": row["Director"],
            "cast": row["Cast"],
            "genre": row["Genre"],
            "plot": row["Plot"],
            "year": row["Release Year"],
            "wiki_page": row["Wiki Page"]
        }

        # actions.append({'index': {'_index': _index, '_id': i}})
        actions.append({'index': {'_index': _index}})
        actions.append(doc)

        if Get_Buffer_Length(actions) > MAX_BYTES:
            response = es.bulk(body=actions)
            print("** indexing ** : {}".format(json.dumps(response, indent=2)))
            del actions[:]

    # --
    # Index for the remain Dataset
    # --
    response = es.bulk(body=actions)
    print("** Remain Dataset indexing ** : {}".format(json.dumps(response, indent=2)))


if __name__ == "__main__":
    '''
    python tools/opensearch/bulk_index_script.py
    '''
    parser = argparse.ArgumentParser(description="Index into Elasticsearch using this script")
    parser.add_argument('-e', '--es', dest='es', default="http://localhost:9250", help='host target')
    args = parser.parse_args()

    if args.es:
        host = args.es

    print('host - ', host)
    # --
    # Instance for the response time log
    es_host = get_es_instance(host)
    # --
    index = "test_omnisearch_v2"

    create_index(es_host, index)

    # sinngle_indexing_mode_run(es_host, index)
    buffer_indexing_mode_run(es_host, index)

    # search
    search(es_host, index)