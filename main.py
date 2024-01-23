from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from config.log_config import create_log
from controller import (es_search_controller,
                        cluster_estimate_controller
                       )

from aiokafka import AIOKafkaConsumer, AIOKafkaProducer
from injector import global_settings
import asyncio

logger = create_log()
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

loop = asyncio.get_event_loop()

# @app.on_event("startup")
async def kafka_event():
    logger.info(f'@@kafka_event starting...@@ --> {global_settings.get_Kafka_Hosts()}, type : {type(global_settings.get_Kafka_Hosts())}')
    
    # poetry add aiokafka = "^0.10.0"
    consumer = AIOKafkaConsumer(global_settings.get_Kafka_topic(), loop=loop, bootstrap_servers=global_settings.get_Kafka_Hosts(),)

    try:
        await consumer.start()
        async for msg in consumer:
            logger.info(f"--message -- {msg}, message : {msg.value.decode('utf-8')}")
            # await kafka_actions[msg.topic](msg)

    except Exception as e:
        print(e)
        return

    finally:
        await consumer.stop()

asyncio.create_task(kafka_event())


''' http://localhost:7777/docs '''

@app.get("/", tags=['API'],  
         status_code=200,
         description="Default GET API", 
         summary="Return Json")
async def root():
    return {"message": "Hello World"}


@app.get("/test", tags=['API'],  
         status_code=200,
         description="Default GET Param API", 
         summary="Return GET Param Json")
async def root_with_arg(id):
    return {"message": "Hello World [{}]".format(id)}


@app.get("/test/{id}", tags=['API'],  
         status_code=200,
         description="Default GET with Body API", 
         summary="Return GET with Body Json")
async def root_with_param(id):
    return {"message": "Hello World [{}]".format(id)}


# router
app.include_router(es_search_controller.app, tags=["Search"], )
app.include_router(cluster_estimate_controller.app, tags=["Cluster"], )