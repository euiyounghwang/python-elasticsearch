
import pytest
from elasticsearch.client import Elasticsearch, IndicesClient
from injector import QueryBuilderInject
import json


def test_build_terms_batch():
        mock_query_handler = QueryBuilderInject
        mock_ids_filter = [
            "111", '222'
        ]
                
        response_ids_filter_query = mock_query_handler.build_terms_filters_batch(_terms=mock_ids_filter, max_terms_count=1)
        assert response_ids_filter_query is not None
        assert response_ids_filter_query == [
            {
                "terms":{
                    "_id":[
                        "111"
                    ]
                }
            },
            {
                "terms":{
                    "_id":[
                        "222"
                    ]
                }
            }
        ]
        
        response_ids_filter_query = mock_query_handler.build_terms_filters_batch(_terms=mock_ids_filter, max_terms_count=5)
        assert response_ids_filter_query is not None
        assert response_ids_filter_query == [
            {
                "terms":{
                    "_id":[
                        "111",
                        "222"
                    ]
                }
            }
        ]
                