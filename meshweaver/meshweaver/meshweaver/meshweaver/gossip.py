import json
import time
import psutil
from typing import Dict

class GossipEngine:
    """Collects local system load and tracks neighbor resource metrics."""
    def __init__(self, node_id: str):
        self.node_id = node_id
        self.cluster_metrics: Dict[str, dict] = {}

    def get_local_metrics(self) -> dict:
        metrics = {
            "node_id": self.node_id,
            "cpu_percent": psutil.cpu_percent(interval=0.1),
            "memory_percent": psutil.virtual_memory().percent,
            "timestamp": time.time()
        }
        self.cluster_metrics[self.node_id] = metrics
        return metrics

    def serialize_gossip(self) -> bytes:
        packet = {"type": "GOSSIP", "metrics": self.get_local_metrics()}
        return json.dumps(packet).encode("utf-8")

    def receive_gossip(self, payload: dict):
        metrics = payload.get("metrics")
        if metrics and "node_id" in metrics:
            self.cluster_metrics[metrics["node_id"]] = metrics
Use code with caution.
