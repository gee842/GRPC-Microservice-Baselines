import Routes_pb2_grpc as pbgrpc
import Routes_pb2 as pbdef
import grpc

with grpc.insecure_channel('localhost:30103') as channel:
    NewServer = pbgrpc.RouteGuideStub(channel)
    print(NewServer)

