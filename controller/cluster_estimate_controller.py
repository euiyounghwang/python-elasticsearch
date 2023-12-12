
from fastapi import APIRouter
from repository.schemas import Search
from injector import (logger, doc)
# from injector import (logger, doc, SearchOmniHandlerInject, QueryBuilderInject)
import json
import datetime

app = APIRouter(
    prefix="/cluster",
)

@app.post("/sharding_predict", description="Cluster sharding predict", summary="Cluster sharding predict")
async def Cluster_sharding_estimate(request: Search):
    ''' Search to Elasticsearch '''
    StartTime, EndTime, Delay_Time = 0, 0, 0
    
    try:
        StartTime = datetime.datetime.now()
        
        # logger.info("api_controller doc: {}".format(json.dumps(doc, indent=2)))
        # request_json = {k : v for k, v in request}
        request_json = request.to_json()
        print(request, type(request), request.size, request_json)
        logger.info("es_search_controller : {}".format(json.dumps(request_json, indent=2)))
        
        EndTime = datetime.datetime.now()

        # return await SearchOmniHandlerInject.search(QueryBuilderInject, oas_query=request_json)
        return {'results' : 
            {
                "the number of primary shards" : 1,
                "the number of replica shards" : 1
            }
        }
    
    finally:
        Delay_Time = str((EndTime - StartTime).seconds) + '.' + str((EndTime - StartTime).microseconds).zfill(6)[:2]
        logger.info('Metrics : {}'.format(Delay_Time))