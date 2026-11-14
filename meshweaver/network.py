import asyncio
import json
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

class MeshUDPProtocol(asyncio.DatagramProtocol):
    """Handles fast non-blocking UDP control messages (PING, PONG)."""
    def __init__(self, message_handler):
        self.message_handler = message_handler
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        asyncio.create_task(self.message_handler(data, addr, self.transport))

class AsyncMeshNetwork:
    def __init__(self, host="127.0.0.1", port=8001):
        self.host = host
        self.port = port
        self.transport = None

    async def start(self, handler):
        loop = asyncio.get_running_loop()
        self.transport, _ = await loop.create_datagram_endpoint(
            lambda: MeshUDPProtocol(handler),
            local_addr=(self.host, self.port)
        )
        logging.info(f"MeshWeaver node active on {self.host}:{self.port}")

    async def ping_peer(self, target_host, target_port):
        ping_msg = json.dumps({"type": "PING", "sender": f"{self.host}:{self.port}"}).encode("utf-8")
        if self.transport:
            self.transport.sendto(ping_msg, (target_host, target_port))
            logging.info(f"Sent PING to {target_host}:{target_port}")
