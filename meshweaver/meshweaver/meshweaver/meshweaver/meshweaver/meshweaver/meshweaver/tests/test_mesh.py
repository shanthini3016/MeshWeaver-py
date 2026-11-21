import KademliaRoutingTable
from meshweaver.gossip import GossipEngine
from meshweaver.router import LoadAwareRouter

def test_cluster_routing():
    dht = KademliaRoutingTable("node-alpha")
    dht.add_peer("node-beta", "127.0.0.1", 8002)
    dht.add_peer("node-gamma", "127.0.0.1", 8003)

    gossip = GossipEngine("node-alpha")
    gossip.receive_gossip({"metrics": {"node_id": "node-beta", "cpu_percent": 65.0, "memory_percent": 50.0}})
    gossip.receive_gossip({"metrics": {"node_id": "node-gamma", "cpu_percent": 18.5, "memory_percent": 40.0}})

    router = LoadAwareRouter(gossip.cluster_metrics)
    selected = router.select_best_node()
    assert selected["node_id"] == "node-gamma"
    print("Integration test passed! Selected lowest load node:", selected["node_id"])

if __name__ == "__main__":
    test_cluster_routing()
Use code with caution.
