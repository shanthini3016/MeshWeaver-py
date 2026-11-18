import Dict, Optional

class LoadAwareRouter:
    """Routes incoming compute tasks to the peer with lowest CPU load."""
    def __init__(self, cluster_metrics: Dict[str, dict]):
        self.cluster_metrics = cluster_metrics

    def select_best_node(self) -> Optional[dict]:
        if not self.cluster_metrics:
            return None
        best_node = min(
            self.cluster_metrics.values(),
            key=lambda m: (m.get("cpu_percent", 100.0), m.get("memory_percent", 100.0))
        )
        return best_node

    def can_accept_locally(self, cpu_threshold: float = 80.0) -> bool:
        if not self.cluster_metrics:
            return True
        avg_cpu = sum(m.get("cpu_percent", 0) for m in self.cluster_metrics.values()) / len(self.cluster_metrics)
        return avg_cpu < cpu_threshold
Use code with caution.
