from rich.console import Console
from rich.table import Table

class MeshDashboard:
    """Renders a live terminal dashboard for cluster node status."""
    def __init__(self):
        self.console = Console()

    def render_cluster_table(self, cluster_metrics: dict):
        table = Table(title="MeshWeaver Live P2P Cluster Status")
        table.add_column("Node ID", style="cyan", no_wrap=True)
        table.add_column("CPU Load (%)", style="magenta")
        table.add_column("RAM Usage (%)", style="green")
        table.add_column("Status", style="bold yellow")

        for node_id, info in cluster_metrics.items():
            table.add_row(
                node_id,
                f"{info.get('cpu_percent', 0):.1f}%",
                f"{info.get('memory_percent', 0):.1f}%",
                "ONLINE"
            )
        self.console.print(table)
Use code with caution.
