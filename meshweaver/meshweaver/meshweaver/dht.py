import hashlib
import time
from typing import Dict, List, Tuple

class KademliaRoutingTable:
    """Decentralized peer discovery table using XOR distance metric."""
    def __init__(self, node_id: str):
        self.node_id = node_id
        self.node_int = int(hashlib.sha1(node_id.encode()).hexdigest(), 16)
        self.peers: Dict[str, dict] = {}

    def xor_distance(self, peer_id: str) -> int:
        peer_int = int(hashlib.sha1(peer_id.encode()).hexdigest(), 16)
        return self.node_int ^ peer_int

    def add_peer(self, peer_id: str, host: str, port: int):
        if peer_id != self.node_id:
            self.peers[peer_id] = {
                "host": host,
                "port": port,
                "last_seen": time.time()
            }

    def get_closest_peers(self, target_id: str, count: int = 3) -> List[Tuple[str, dict]]:
        sorted_peers = sorted(
            self.peers.items(),
            key=lambda item: self.xor_distance(item[0])
        )
        return sorted_peers[:count]
Use code with caution.
