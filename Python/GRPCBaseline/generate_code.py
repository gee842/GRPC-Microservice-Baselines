"""Runs protoc with the gRPC plugin to generate messages and gRPC stubs."""

from grpc_tools import protoc
proto_files = ["../../service-definitions/Routes.proto"]


for file in proto_files:
    protoc.main([
        'grpc_tools.protoc',
        '--proto_path=../../service-definitions/',
        '--python_out=.',
        '--grpc_python_out=.',
        file
    ])