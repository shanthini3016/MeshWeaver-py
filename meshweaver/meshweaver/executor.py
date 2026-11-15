import cloudpickle
import logging

class TaskSerializer:
    """Serializes and executes Python functions across peer nodes."""
    @staticmethod
    def pack_task(func, *args, **kwargs) -> bytes:
        payload = {
            "type": "TASK",
            "func": func,
            "args": args,
            "kwargs": kwargs
        }
        return cloudpickle.dumps(payload)

    @staticmethod
    def unpack_and_run(raw_bytes: bytes):
        try:
            payload = cloudpickle.loads(raw_bytes)
            if payload.get("type") == "TASK":
                result = payload["func"](*payload.get("args", ()), **payload.get("kwargs", {}))
                logging.info(f"Executed remote task successfully. Result: {result}")
                return result
        except Exception as exc:
            logging.error(f"Remote task execution failed: {exc}")
            return None
Use code with caution.
