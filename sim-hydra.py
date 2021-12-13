from __future__ import annotations

import argparse
import dataclasses
import heapq
import logging
import os
import numpy as np
import pickle as pkl
import pprint

from hydralib import *


# TODO: fix syspath variable

# TODO: move workload to common.py
@dataclasses.dataclass
class Workload:
    session: ModelSession
    avg_rps: float
    num_gpus: int
    

class Simulation:
    @staticmethod
    def parse_args() -> argparse.Namespace:
        parser = argparse.ArgumentParser()
        parser.add_argument("--profile_dir")
        parser.add_argument(
            "--workloads",
            help="<framework>:<model>:<slo_ms>@avg_rps=<float>,num_backends=<int>[,num_backups=<int>]",
            required=True,
            nargs="*",
        )
        parser.add_argument("--log_prefix")
        parser.add_argument("--num_frontends", type=int, required=True)
        parser.add_argument("--num_backends", type=int, required=True)
        parser.add_argument("--num_shared_backups", type=int, default=0)
        parser.add_argument("--gap", required=True)
        parser.add_argument("--warmup", type=int, required=True)
        parser.add_argument("--duration", type=int, required=True)
        parser.add_argument(
            "--dispatcher",
            choices=[
                "randomrr",
                "simple",
                "simple_clockwork",
                "clockwork",
                "fullshared",
                "batchplan",
                "fixedleft",
                "delaydrop",
                "bubble",
                "delayed",
                "rankmt",
            ],
            required=True,
        )
        parser.add_argument("--repeats", type=int, default=1)
        parser.add_argument("--parallel", action="store_true")
        parser.add_argument("--no_network_latency", action="store_true")
        parser.add_argument("--hack_one_shot_cycle_delay", type=float, default=0.25)
        parser.add_argument("--bse_xrps", type=float, default=1.0)
        parser.add_argument("--bse_xstd", type=float, default=0.0)
        args = parser.parse_args()
        return args


def main():
    args = Simulation.parse_args()

if __name__ == "__main__":
    main()