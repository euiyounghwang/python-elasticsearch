from __future__ import print_function

import grpc

from api import GreeterServicer
from protos import helloworld_pb2_grpc, helloworld_pb2

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = helloworld_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(helloworld_pb2.HelloRequest(name='python'))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    run()