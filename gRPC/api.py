from protos import helloworld_pb2_grpc, helloworld_pb2
import json
import logging

logging.basicConfig(format='%(asctime)s - %(message)s',level=logging.DEBUG)


class GreeterServicer(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        logging.info(f"GreeterServicer.Sayhello() was called ! : {request}")
        test_json = {
            'a' : 1,
            'b' : 2
        }
        return helloworld_pb2.HelloReply(
            # message=f"hello {request.name}"
            message=f"{test_json}"
        )