from __future__ import print_function

import grpc

from api import GreeterServicer, logging
from protos import helloworld_pb2_grpc, helloworld_pb2
import json


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = helloworld_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(helloworld_pb2.HelloRequest(name='python'))
    logging.info("Greeter client received: " + response.message)
    logging.info(f"Greeter client received type: {type(response.message)}")
    result = json.loads(str(response.message).replace("'", '"'))
    logging.info(f"Greeter client converted type: {type(result)}")
    logging.info(f"Greeter client converted type: {json.dumps(result, indent=2)}")


if __name__ == '__main__':
    run()