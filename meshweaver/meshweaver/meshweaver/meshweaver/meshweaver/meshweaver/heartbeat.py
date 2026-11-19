import time
import logging
from typing import Dict, List

class HeartbeatMonitor:
    """Detects dead peers and triggers task re-routing on timeout."""
    def __init__(self, timeout_seconds: float = 15.0):
        self.timeout_seconds = timeout_seconds
        self.heartbeats: Dict[str, float] = {}

    def record_heartbeat(self, node_id: str):
        self.heartbeats[node_id] = time.time()

    def get_dead_nodes(self) -> List[str]:
        now = time.time()
        dead = [
            node_id for node_id, last_ping in self.heartbeats.items()
            if (now - last_ping) > self.timeout_seconds
        ]
        for node_id in dead:
            logging.warning(f"Node '{node_id}' missed heartbeat! Marking offline.")
            del self.heartbeats[node_id]
        return dead
Use code with caution.
