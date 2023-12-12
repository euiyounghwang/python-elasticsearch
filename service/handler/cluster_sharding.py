
import json

class ClusterShardingHandler(object):
    ''' 
    You will want to limit your maximum shard size to 30-80 GB if running a recent version of Elasticsearch. 
    In fact, a single shard can hold as much as 100s of GB and still perform well. (If running below version 6.0 then estimate 30-50 GB.) 
    
    Using the 30-80 GB value, you can calculate how many shards you’ll need.
    
    For instance, let’s assume you rotate indices monthly and expect around 600 GB of data per month. 
    In this example, you would allocate 8 to 20 shards.
    '''
    
    def __init__(self, es_client, logger):
        self.es_client = es_client
        self.logger = logger
        
    async def sharding_predict(self, oas_query=None):
        ''' Search with QuerBuilder '''
        if not oas_query:
            oas_query = {}
            
        sharding_results = {'results' : 
            {
                "the number of primary shards" : 1,
                "the number of replica shards" : 1
            }
        }
        
        self.logger.info(json.dumps(sharding_results, indent=2))
                
        return sharding_results
    
    