from __future__ import annotations

import dataclasses
from typing import (
    Set,
    Dict,
    NewType,
)

__all__ = [
    "NodeID",
    "RequestID",
    "LocalID",
    "QueryID",
    "ModelSession",
    "ModelRoute",
    "ModelRoutes",
]

NodeID = NewType("NodeID", str)
RequestID = NewType("RequestID", int)
LocalID = NewType("LocalID", int)
QueryID = NewType("QueryID", int)

@dataclasses.dataclass(frozen=True, order=True)
class ModelSession:
    framework: str
    model: str
    slo_ms: int

    def __str__(self):
        return f"{self.framework}:{self.model}:{self.slo_ms}"


@dataclasses.dataclass
class ModelRoute:
    rps_hint: float
    backend_rates: Dict[NodeID, float] = dataclasses.field(default_factory=dict)


@dataclasses.dataclass
class ModelRoutes:
    primaries: Dict[ModelSession, ModelRoute] = dataclasses.field(default_factory=dict)
    backups: Set[NodeID] = dataclasses.field(default_factory=set)