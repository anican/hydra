from __future__ import annotations

import dataclasses
from typing import List, Optional

from .data import (
    ModelSession, 
    LocalID, 
    NodeID, 
    QueryID, 
    RequestID
)

__all__ = [
    "AbstractPacket",
    "ClientRequest",
    "DispatchRpcRequest",
    "DispatchRpcReply",
    "QueryRpcRequest",
    "QueryRpcReply",
    "BackendExecStartMessage",
    "BackendBatchCompletionMessage",
    "BackendSetOneShotCycleCommand",
    "BackendSetBatchPlanCommand",
]


@dataclasses.dataclass
class Packet:
    source: NodeID
    target: NodeID


@dataclasses.dataclass
class ClientRequest(Packet):
    request_id: RequestID
    model_session: ModelSession


@dataclasses.dataclass
class DispatchRpcRequest(Packet):
    local_id: LocalID
    model_session: ModelSession
    frontend_recv_time: float


@dataclasses.dataclass
class DispatchRpcReply(Packet):
    local_id: LocalID
    query_id: QueryID
    backend_id: Optional[NodeID]


@dataclasses.dataclass
class QueryRpcRequest(Packet):
    query_id: QueryID
    model_session: ModelSession
    frontend_recv_time: float


@dataclasses.dataclass
class QueryRpcReply(Packet):
    @dataclasses.dataclass
    class Result:
        query_id: QueryID
        success: bool
        frontend_recv_time: float
        backend_recv_time: float
        backend_exec_time: float
        backend_reply_time: float
        backend_batch_size: int

    results: List[QueryRpcReply.Result]


@dataclasses.dataclass
class BackendExecStartMessage(Packet):
    start_time: float
    estimate_exec_elapse: float
    cnt_drops: int
    batch_size: int
    remain_qlen: int


@dataclasses.dataclass
class BackendBatchCompletionMessage(Packet):
    start_time: float
    exec_elapse: float


@dataclasses.dataclass
class BackendSetOneShotCycleCommand(Packet):
    seqnum: int
    model_session: ModelSession
    start_time_hint: Optional[float]


@dataclasses.dataclass
class BackendSetBatchPlanCommand(Packet):
    plan_id: int
    model_session: ModelSession
    exec_time: float
    query_ids: List[QueryID]