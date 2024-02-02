
from fastapi import APIRouter
from repository.schemas import Search
from injector import (logger, doc, SearchOmniHandlerInject, QueryBuilderInject, UDP_SOC)
from service.handler.status_handler import (StatusHanlder, StatusException)
import json
import datetime

app = APIRouter(
    prefix="/es",
)


@app.post("/health", 
          status_code=StatusHanlder.HTTP_STATUS_200,
          description="Search to ES", 
          summary="Search to ES")
async def Elasticsearch_Search():
    response = SearchOmniHandlerInject.get_es_health()
    logger.info('SearchOmniHandler:get_es_info - {}'.format(response))
    return await response


@app.post("/search", 
          status_code=StatusHanlder.HTTP_STATUS_200,
          description="Search to ES", 
          summary="Search to ES")
async def Elasticsearch_Search(request: Search):
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

        return await SearchOmniHandlerInject.search(QueryBuilderInject, oas_query=request_json)
    
    except Exception as e:
        logger.error(e)
        return StatusException.raise_exception(e)
    
    finally:
        UDP_SOC.socket_logstash_handler(request.to_json())
        
        Delay_Time = str((EndTime - StartTime).seconds) + '.' + str((EndTime - StartTime).microseconds).zfill(6)[:2]
        logger.info('Metrics : {}'.format(Delay_Time))
        
     

    