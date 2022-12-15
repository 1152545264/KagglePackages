# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from tensorboard.data.proto import data_provider_pb2 as tensorboard_dot_data_dot_proto_dot_data__provider__pb2


class TensorBoardDataProviderStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetExperiment = channel.unary_unary(
        '/tensorboard.data.TensorBoardDataProvider/GetExperiment',
        request_serializer=tensorboard_dot_data_dot_proto_dot_data__provider__pb2.GetExperimentRequest.SerializeToString,
        response_deserializer=tensorboard_dot_data_dot_proto_dot_data__provider__pb2.GetExperimentResponse.FromString,
        )
    self.ListPlugins = channel.unary_unary(
        '/tensorboard.data.TensorBoardDataProvider/ListPlugins',
        request_serializer=tensorboard_dot_data_dot_proto_dot_data__provider__pb2.ListPluginsRequest.SerializeToString,
        response_deserializer=tensorboard_dot_data_dot_proto_dot_data__provider__pb2.ListPluginsResponse.FromString,
        )
    self.ListRuns = channel.unary_unary(
        '/tensorboard.data.TensorBoardDataProvider/ListRuns',
        request_serializer=tensorboard_dot_data_dot_proto_dot_data__provider__pb2.ListRunsRequest.SerializeToString,
        response_deserializer=tensorboard_dot_data_dot_proto_dot_data__provider__pb2.ListRunsResponse.FromString,
        )
    self.ListScalars = channel.unary_unary(
        '/tensorboard.data.TensorBoardDataProvider/ListScalars',
        request_serializer=tensorboard_dot_data_dot_proto_dot_data__provider__pb2.ListScalarsRequest.SerializeToString,
        response_deserializer=tensorboard_dot_data_dot_proto_dot_data__provider__pb2.ListScalarsResponse.FromString,
        )
    self.ReadScalars = channel.unary_unary(
        '/tensorboard.data.TensorBoardDataProvider/ReadScalars',
        request_serializer=tensorboard_dot_data_dot_proto_dot_data__provider__pb2.ReadScalarsRequest.SerializeToString,
        response_deserializer=tensorboard_dot_data_dot_proto_dot_data__provider__pb2.ReadScalarsResponse.FromString,
        )
    self.ListTensors = channel.unary_unary(
        '/tensorboard.data.TensorBoardDataProvider/ListTensors',
        request_serializer=tensorboard_dot_data_dot_proto_dot_data__provider__pb2.ListTensorsRequest.SerializeToString,
        response_deserializer=tensorboard_dot_data_dot_proto_dot_data__provider__pb2.ListTensorsResponse.FromString,
        )
    self.ReadTensors = channel.unary_unary(
        '/tensorboard.data.TensorBoardDataProvider/ReadTensors',
        request_serializer=tensorboard_dot_data_dot_proto_dot_data__provider__pb2.ReadTensorsRequest.SerializeToString,
        response_deserializer=tensorboard_dot_data_dot_proto_dot_data__provider__pb2.ReadTensorsResponse.FromString,
        )
    self.ListBlobSequences = channel.unary_unary(
        '/tensorboard.data.TensorBoardDataProvider/ListBlobSequences',
        request_serializer=tensorboard_dot_data_dot_proto_dot_data__provider__pb2.ListBlobSequencesRequest.SerializeToString,
        response_deserializer=tensorboard_dot_data_dot_proto_dot_data__provider__pb2.ListBlobSequencesResponse.FromString,
        )
    self.ReadBlobSequences = channel.unary_unary(
        '/tensorboard.data.TensorBoardDataProvider/ReadBlobSequences',
        request_serializer=tensorboard_dot_data_dot_proto_dot_data__provider__pb2.ReadBlobSequencesRequest.SerializeToString,
        response_deserializer=tensorboard_dot_data_dot_proto_dot_data__provider__pb2.ReadBlobSequencesResponse.FromString,
        )
    self.ReadBlob = channel.unary_stream(
        '/tensorboard.data.TensorBoardDataProvider/ReadBlob',
        request_serializer=tensorboard_dot_data_dot_proto_dot_data__provider__pb2.ReadBlobRequest.SerializeToString,
        response_deserializer=tensorboard_dot_data_dot_proto_dot_data__provider__pb2.ReadBlobResponse.FromString,
        )


class TensorBoardDataProviderServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetExperiment(self, request, context):
    """Get metadata about an experiment.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListPlugins(self, request, context):
    """List plugins that have data for an experiment.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListRuns(self, request, context):
    """List runs within an experiment.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListScalars(self, request, context):
    """List metadata about scalar time series.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReadScalars(self, request, context):
    """Read data from scalar time series.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListTensors(self, request, context):
    """List metadata about tensor time series.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReadTensors(self, request, context):
    """Read data from tensor time series.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListBlobSequences(self, request, context):
    """List metadata about blob sequence time series.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReadBlobSequences(self, request, context):
    """Read blob references from blob sequence time series. See `ReadBlob` to read
    the actual blob data.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReadBlob(self, request, context):
    """Read data for a specific blob.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TensorBoardDataProviderServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetExperiment': grpc.unary_unary_rpc_method_handler(
          servicer.GetExperiment,
          request_deserializer=tensorboard_dot_data_dot_proto_dot_data__provider__pb2.GetExperimentRequest.FromString,
          response_serializer=tensorboard_dot_data_dot_proto_dot_data__provider__pb2.GetExperimentResponse.SerializeToString,
      ),
      'ListPlugins': grpc.unary_unary_rpc_method_handler(
          servicer.ListPlugins,
          request_deserializer=tensorboard_dot_data_dot_proto_dot_data__provider__pb2.ListPluginsRequest.FromString,
          response_serializer=tensorboard_dot_data_dot_proto_dot_data__provider__pb2.ListPluginsResponse.SerializeToString,
      ),
      'ListRuns': grpc.unary_unary_rpc_method_handler(
          servicer.ListRuns,
          request_deserializer=tensorboard_dot_data_dot_proto_dot_data__provider__pb2.ListRunsRequest.FromString,
          response_serializer=tensorboard_dot_data_dot_proto_dot_data__provider__pb2.ListRunsResponse.SerializeToString,
      ),
      'ListScalars': grpc.unary_unary_rpc_method_handler(
          servicer.ListScalars,
          request_deserializer=tensorboard_dot_data_dot_proto_dot_data__provider__pb2.ListScalarsRequest.FromString,
          response_serializer=tensorboard_dot_data_dot_proto_dot_data__provider__pb2.ListScalarsResponse.SerializeToString,
      ),
      'ReadScalars': grpc.unary_unary_rpc_method_handler(
          servicer.ReadScalars,
          request_deserializer=tensorboard_dot_data_dot_proto_dot_data__provider__pb2.ReadScalarsRequest.FromString,
          response_serializer=tensorboard_dot_data_dot_proto_dot_data__provider__pb2.ReadScalarsResponse.SerializeToString,
      ),
      'ListTensors': grpc.unary_unary_rpc_method_handler(
          servicer.ListTensors,
          request_deserializer=tensorboard_dot_data_dot_proto_dot_data__provider__pb2.ListTensorsRequest.FromString,
          response_serializer=tensorboard_dot_data_dot_proto_dot_data__provider__pb2.ListTensorsResponse.SerializeToString,
      ),
      'ReadTensors': grpc.unary_unary_rpc_method_handler(
          servicer.ReadTensors,
          request_deserializer=tensorboard_dot_data_dot_proto_dot_data__provider__pb2.ReadTensorsRequest.FromString,
          response_serializer=tensorboard_dot_data_dot_proto_dot_data__provider__pb2.ReadTensorsResponse.SerializeToString,
      ),
      'ListBlobSequences': grpc.unary_unary_rpc_method_handler(
          servicer.ListBlobSequences,
          request_deserializer=tensorboard_dot_data_dot_proto_dot_data__provider__pb2.ListBlobSequencesRequest.FromString,
          response_serializer=tensorboard_dot_data_dot_proto_dot_data__provider__pb2.ListBlobSequencesResponse.SerializeToString,
      ),
      'ReadBlobSequences': grpc.unary_unary_rpc_method_handler(
          servicer.ReadBlobSequences,
          request_deserializer=tensorboard_dot_data_dot_proto_dot_data__provider__pb2.ReadBlobSequencesRequest.FromString,
          response_serializer=tensorboard_dot_data_dot_proto_dot_data__provider__pb2.ReadBlobSequencesResponse.SerializeToString,
      ),
      'ReadBlob': grpc.unary_stream_rpc_method_handler(
          servicer.ReadBlob,
          request_deserializer=tensorboard_dot_data_dot_proto_dot_data__provider__pb2.ReadBlobRequest.FromString,
          response_serializer=tensorboard_dot_data_dot_proto_dot_data__provider__pb2.ReadBlobResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'tensorboard.data.TensorBoardDataProvider', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))