
#### gRPC (gRPC Remote Procedure Calls)
- gRPC was initially created by Google
- gRPC is a modern open source high performance Remote Procedure Call (RPC) framework that can run in any environment
- Service jeong-uiga dansunhada
​- It can be used in multiple programming languages and platforms
- Two-way streaming data processing is possible
- Python 3.5 or higher or pip version 9.0.1 or higher

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
```bash

cd ./gRPC/protos
python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. helloworld.proto
```
