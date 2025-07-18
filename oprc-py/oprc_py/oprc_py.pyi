# This file is automatically generated by pyo3_stub_gen
# ruff: noqa: E501, F401

import builtins
import typing
from enum import Enum

class DataManager:
    r"""
    Manages data operations for objects, interacting with an object proxy.
    """
    def get_obj(self, cls_id:builtins.str, partition_id:builtins.int, obj_id:builtins.int) -> typing.Any:
        r"""
        Retrieves an object by its class ID, partition ID, and object ID. (Synchronous)
        
        # Arguments
        
        * `cls_id`: The class ID of the object.
        * `partition_id`: The partition ID where the object resides.
        * `obj_id`: The unique ID of the object.
        
        # Returns
        
        A `PyResult` containing the Python representation of the object if found,
        or `None` if the object does not exist.
        """
    def get_obj_async(self, cls_id:builtins.str, partition_id:builtins.int, obj_id:builtins.int) -> typing.Any:
        r"""
        Retrieves an object by its class ID, partition ID, and object ID. (Asynchronous)
        
        # Arguments
        
        * `cls_id`: The class ID of the object.
        * `partition_id`: The partition ID where the object resides.
        * `obj_id`: The unique ID of the object.
        
        # Returns
        
        A `PyResult` containing the Python representation of the object if found,
        or `None` if the object does not exist.
        """
    def set_obj(self, obj:ObjectData) -> None:
        r"""
        Sets (creates or updates) an object. (Synchronous)
        
        # Arguments
        
        * `obj`: A Python `ObjectData` instance representing the object to be set.
        
        # Returns
        
        A `PyResult` indicating success or failure.
        """
    def set_obj_async(self, obj:ObjectData) -> None:
        r"""
        Sets (creates or updates) an object. (Asynchronous)
        
        # Arguments
        
        * `obj`: A Python `ObjectData` instance representing the object to be set.
        
        # Returns
        
        A `PyResult` indicating success or failure.
        """
    def del_obj(self, cls_id:builtins.str, partition_id:builtins.int, obj_id:builtins.int) -> None:
        r"""
        Deletes an object by its class ID, partition ID, and object ID. (Synchronous)
        
        # Arguments
        
        * `cls_id`: The class ID of the object.
        * `partition_id`: The partition ID where the object resides.
        * `obj_id`: The unique ID of the object.
        
        # Returns
        
        A `PyResult` indicating success or failure.
        """
    def del_obj_async(self, cls_id:builtins.str, partition_id:builtins.int, obj_id:builtins.int) -> None:
        r"""
        Deletes an object by its class ID, partition ID, and object ID. (Asynchronous)
        
        # Arguments
        
        * `cls_id`: The class ID of the object.
        * `partition_id`: The partition ID where the object resides.
        * `obj_id`: The unique ID of the object.
        
        # Returns
        
        A `PyResult` indicating success or failure.
        """

class InvocationRequest:
    r"""
    Represents a request to invoke a function.
    """
    partition_id: builtins.int
    cls_id: builtins.str
    fn_id: builtins.str
    options: builtins.dict[builtins.str, builtins.str]
    payload: builtins.list[builtins.int]
    def __new__(cls, cls_id:builtins.str, fn_id:builtins.str, partition_id:builtins.int=0, options:typing.Mapping[builtins.str, builtins.str]={}, payload:typing.Sequence[builtins.int]=b'') -> InvocationRequest:
        r"""
        Creates a new `InvocationRequest`.
        """

class InvocationResponse:
    r"""
    Represents the response of an invocation.
    """
    payload: builtins.list[builtins.int]
    status: builtins.int
    header: builtins.dict[builtins.str, builtins.str]
    def __new__(cls, payload:typing.Sequence[builtins.int]=b'', status:builtins.int=0, header:typing.Mapping[builtins.str, builtins.str]={}) -> InvocationResponse:
        r"""
        Creates a new `InvocationResponse`.
        """
    def __str__(self) -> builtins.str:
        r"""
        Returns a string representation of the `InvocationResponse`.
        """

class OaasEngine:
    r"""
    Represents the OaasEngine, which manages data, RPC, and Zenoh sessions.
    """
    data_manager: DataManager
    rpc_manager: RpcManager
    def __new__(cls) -> OaasEngine:
        r"""
        Creates a new instance of OaasEngine.
        Initializes the Tokio runtime, Zenoh session, DataManager, and RpcManager.
        """
    def serve_grpc_server_async(self, port:builtins.int, event_loop:typing.Any, callback:typing.Any) -> None:
        r"""
        Starts a gRPC server on the specified port.
        
        # Arguments
        
        * `port` - The port number to bind the gRPC server to.
        * `event_loop` - The Python event loop.
        * `callback` - The Python callback function to handle invocations.
        """
    def serve_grpc_server(self, port:builtins.int, callback:typing.Any) -> None:
        r"""
        Starts a gRPC server on the specified port.
        
        # Arguments
        
        * `port` - The port number to bind the gRPC server to.
        * `callback` - The Python callback function to handle invocations.
        """
    def serve_function(self, key_expr:builtins.str, event_loop:typing.Any, callback:typing.Any) -> None:
        r"""
        Serves a function over Zenoh.
        
        # Arguments
        
        * `key_expr` - The Zenoh key expression to serve the function on.
        * `event_loop` - The Python event loop.
        * `callback` - The Python callback function to handle invocations.
        """
    def stop_function(self, key_expr:builtins.str) -> None:
        r"""
        Stops a function being served over Zenoh.
        
        # Arguments
        
        * `key_expr` - The Zenoh key expression of the function to stop.
        """
    def stop_server(self) -> None:
        r"""
        Stops the gRPC server.
        """

class ObjectData:
    r"""
    Represents the data of an object, including its metadata, entries, and event.
    """
    meta: ObjectMetadata
    entries: builtins.dict[builtins.int, builtins.list[builtins.int]]
    event: typing.Optional[PyObjectEvent]
    def __new__(cls, meta:ObjectMetadata, entries:typing.Mapping[builtins.int, typing.Sequence[builtins.int]]={}, event:typing.Optional[PyObjectEvent]=None) -> ObjectData:
        r"""
        Creates a new `ObjectData`.
        """
    def copy(self) -> ObjectData:
        r"""
        Creates a clone of this `ObjectData`.
        """

class ObjectInvocationRequest:
    r"""
    Represents a request to invoke a function on an object.
    """
    partition_id: builtins.int
    cls_id: builtins.str
    fn_id: builtins.str
    object_id: builtins.int
    options: builtins.dict[builtins.str, builtins.str]
    payload: builtins.list[builtins.int]
    def __new__(cls, cls_id:builtins.str, fn_id:builtins.str, object_id:builtins.int, partition_id:builtins.int=0, options:typing.Mapping[builtins.str, builtins.str]={}, payload:typing.Sequence[builtins.int]=b'') -> ObjectInvocationRequest:
        r"""
        Creates a new `ObjectInvocationRequest`.
        """

class ObjectMetadata:
    r"""
    Represents the metadata of an object.
    """
    object_id: builtins.int
    cls_id: builtins.str
    partition_id: builtins.int
    def __new__(cls, cls_id:builtins.str, partition_id:builtins.int, object_id:builtins.int) -> ObjectMetadata:
        r"""
        Creates a new `ObjectMetadata`.
        """
    def __str__(self) -> builtins.str: ...

class PyDataTriggerEntry:
    r"""
    Represents the trigger entries for a specific data event, wrapping `oprc_pb::DataTriggerEntry`.
    """
    on_create: builtins.list[PyTriggerTarget]
    r"""
    List of targets to trigger on data creation.
    """
    on_update: builtins.list[PyTriggerTarget]
    r"""
    List of targets to trigger on data update.
    """
    on_delete: builtins.list[PyTriggerTarget]
    r"""
    List of targets to trigger on data deletion.
    """
    def __str__(self) -> builtins.str:
        r"""
        Returns a string representation of the `PyDataTriggerEntry`.
        """

class PyFuncTriggerEntry:
    r"""
    Represents the trigger entries for a specific function event, wrapping `oprc_pb::FuncTriggerEntry`.
    """
    on_complete: builtins.list[PyTriggerTarget]
    r"""
    List of targets to trigger on function completion.
    """
    on_error: builtins.list[PyTriggerTarget]
    r"""
    List of targets to trigger on function error.
    """
    def __str__(self) -> builtins.str:
        r"""
        Returns a string representation of the `PyFuncTriggerEntry`.
        """

class PyObjectEvent:
    r"""
    Represents an event associated with an object, wrapping the protobuf `ObjectEvent`.
    """
    def __new__(cls) -> PyObjectEvent:
        r"""
        Creates a new, empty `PyObjectEvent`.
        """
    def __str__(self) -> builtins.str:
        r"""
        Returns a string representation of the `PyObjectEvent`.
        """
    def manage_fn_trigger(self, source_fn_id:builtins.str, trigger:PyTriggerTarget, event_type:FnTriggerType, add_action:builtins.bool) -> builtins.bool:
        r"""
        Manages function triggers by adding or removing a trigger target for a specific function and event type.
        
        # Arguments
        * `source_fn_id` - The function ID that will trigger the event
        * `trigger` - The target to be triggered
        * `event_type` - When to trigger (on completion or on error)
        * `add_action` - Whether to add (true) or remove (false) the trigger
        
        # Returns
        * `true` if the operation was successful (trigger added or removed)
        * `false` if the operation failed (trigger already exists or not found)
        """
    def manage_data_trigger(self, source_key:builtins.int, trigger:PyTriggerTarget, event_type:DataTriggerType, add_action:builtins.bool) -> builtins.bool:
        r"""
        Manages data triggers by adding or removing a trigger target for a specific data key and event type.
        
        # Arguments
        * `source_key` - The data key ID that will trigger the event
        * `trigger` - The target to be triggered
        * `event_type` - When to trigger (on create, update, or delete)
        * `add_action` - Whether to add (true) or remove (false) the trigger
        
        # Returns
        * `true` if the operation was successful (trigger added or removed)
        * `false` if the operation failed (trigger already exists or not found)
        """
    def get_func_triggers(self) -> builtins.dict[builtins.str, PyFuncTriggerEntry]:
        r"""
        Gets the function triggers associated with this event.
        
        Returns a map where keys are source function IDs and values are `PyFuncTriggerEntry` objects.
        """
    def get_data_triggers(self) -> builtins.dict[builtins.int, PyDataTriggerEntry]:
        r"""
        Gets the data triggers associated with this event.
        
        Returns a map where keys are source data key IDs and values are `PyDataTriggerEntry` objects.
        """

class PyTriggerTarget:
    r"""
    Represents a target for a trigger, wrapping the protobuf `TriggerTarget`.
    """
    cls_id: builtins.str
    r"""
    Gets the class ID of the trigger target.
    """
    partition_id: builtins.int
    r"""
    Gets the partition ID of the trigger target.
    """
    fn_id: builtins.str
    r"""
    Gets the function ID of the trigger target.
    """
    object_id: typing.Optional[builtins.int]
    r"""
    Gets the object ID of the trigger target, if any.
    """
    req_options: builtins.dict[builtins.str, builtins.str]
    r"""
    Gets the request options for the trigger target.
    """
    def __new__(cls, cls_id:builtins.str, partition_id:builtins.int, fn_id:builtins.str, object_id:typing.Optional[builtins.int]=None, req_options:typing.Mapping[builtins.str, builtins.str]={}) -> PyTriggerTarget:
        r"""
        Creates a new `PyTriggerTarget`.
        """
    def __str__(self) -> builtins.str:
        r"""
        Returns a string representation of the `PyTriggerTarget`.
        """
    def set_cls_id(self, cls_id:builtins.str) -> None:
        r"""
        Sets the class ID of the trigger target.
        """
    def set_partition_id(self, partition_id:builtins.int) -> None:
        r"""
        Sets the partition ID of the trigger target.
        """
    def set_fn_id(self, fn_id:builtins.str) -> None:
        r"""
        Sets the function ID of the trigger target.
        """
    def set_object_id(self, object_id:typing.Optional[builtins.int]) -> None:
        r"""
        Sets the object ID of the trigger target.
        """
    def set_req_options(self, req_options:typing.Mapping[builtins.str, builtins.str]) -> None:
        r"""
        Sets the request options for the trigger target.
        """

class RpcManager:
    r"""
    Manages RPC invocations using an ObjectProxy.
    """
    def invoke_fn(self, req:InvocationRequest) -> InvocationResponse:
        r"""
        Invokes a function based on the provided InvocationRequest. (Synchronous)
        
        # Arguments
        
        * `py`: The Python GIL token.
        * `req`: A Python `InvocationRequest` instance.
        
        # Returns
        
        A `PyResult` containing an `InvocationResponse`.
        """
    def invoke_fn_async(self, req:InvocationRequest) -> InvocationResponse:
        r"""
        Invokes a function based on the provided InvocationRequest. (Asynchronous)
        
        # Arguments
        
        * `req`: A Python `InvocationRequest` instance.
        
        # Returns
        
        A `PyResult` containing an `InvocationResponse`.
        """
    def invoke_obj(self, req:ObjectInvocationRequest) -> InvocationResponse:
        r"""
        Invokes an object method based on the provided ObjectInvocationRequest. (Synchronous)
        
        # Arguments
        
        * `py`: The Python GIL token.
        * `req`: A Python `ObjectInvocationRequest` instance.
        
        # Returns
        
        A `PyResult` containing an `InvocationResponse`.
        """
    def invoke_obj_async(self, req:ObjectInvocationRequest) -> InvocationResponse:
        r"""
        Invokes an object method based on the provided ObjectInvocationRequest. (Asynchronous)
        
        # Arguments
        
        * `req`: A Python `ObjectInvocationRequest` instance.
        
        # Returns
        
        A `PyResult` containing an `InvocationResponse`.
        """

class DataTriggerType(Enum):
    OnCreate = ...
    OnUpdate = ...
    OnDelete = ...

class FnTriggerType(Enum):
    OnComplete = ...
    OnError = ...

class InvocationResponseCode(Enum):
    r"""
    Represents the status code of an invocation response.
    """
    Okay = ...
    InvalidRequest = ...
    AppError = ...
    SystemError = ...

def init_logger(level:builtins.str, raise_error:builtins.bool) -> None: ...

