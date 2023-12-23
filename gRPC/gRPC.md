
#### gRPC (gRPC Remote Procedure Calls)
- gRPC was initially created by Google
- gRPC is a modern open source high performance Remote Procedure Call (RPC) framework that can run in any environment
​- It can be used in multiple programming languages and platforms
- Two-way streaming data processing is possible
- Python 3.5 or higher or pip version 9.0.1 or higher
- gRPC support HTTP2 (REST : HTTP1.1)
- Loadbalancer should be support HTTP/2

#### gRCP Install
```bash

https://dailyheumsi.tistory.com/268

poetry add grpcio
poetry add grpcio-tools

pip list | grep grpcio

# VS-Code Install Package
vscode-proto3
```


#### gRCP Python File Generate
Now, to generate Python code from the protobufs, run the following:
This generates several Python files from the .proto file. Here’s a breakdown:
- python -m grpc_tools.protoc runs the protobuf compiler, which will generate Python code from the protobuf code.
- -I ../protobufs tells the compiler where to find files that your protobuf code imports. You don’t actually use the import feature, but the -I flag is required nonetheless.
- --python_out=. --grpc_python_out=. tells the compiler where to output the Python files. As you’ll see shortly, it will generate two files, and you could put each in a separate directory with these options if you wanted to.
- ../protobufs/recommendations.proto is the path to the protobuf file, which will be used to generate the Python code.
```bash

cd ./gRPC/protos
python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. helloworld.proto
```
