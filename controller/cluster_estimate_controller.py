
from fastapi import APIRouter
from repository.schemas import Performance
from injector import (logger, doc)
from injector import (logger, 
                      doc, 
                      SearchOmniHandlerInject, 
                      QueryBuilderInject, 
                      ClusterShardingInject)
from service.handler.status_handler import (StatusHanlder, StatusException)
import json
import datetime

app = APIRouter(
    prefix="/cluster",
)

@app.post("/sharding_predict", description="Cluster sharding predict", summary="Cluster sharding predict")
async def Cluster_sharding_estimate(request: Performance):
    ''' Search to Elasticsearch '''
    StartTime, EndTime, Delay_Time = 0, 0, 0
    
    try:
        StartTime = datetime.datetime.now()
        
        # logger.info("api_controller doc: {}".format(json.dumps(doc, indent=2)))
        # request_json = {k : v for k, v in request}
        request_json = request.to_json()
        print(request, type(request), request.data_size, request_json)
        logger.info("Cluster_sharding_estimate_Controller : {}".format(json.dumps(request_json, indent=2)))
        
        EndTime = datetime.datetime.now()

        return await ClusterShardingInject.sharding_predict(oas_query=request_json)
       
    except Exception as e:
        logger.error(e)
        return StatusException.raise_exception(e)
    
    finally:
        Delay_Time = str((EndTime - StartTime).seconds) + '.' + str((EndTime - StartTime).microseconds).zfill(6)[:2]
        logger.info('Metrics : {}'.format(Delay_Time))