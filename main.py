from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from config.log_config import create_log
from controller import (es_search_controller,
                        cluster_estimate_controller
                       )

logger = create_log()
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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