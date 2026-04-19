import time
from typing import Any, Dict, Optional

_CACHE: Dict[str, Dict[str, Any]] = {}

def get_cached(key: str, ttl_seconds: int = 900) -> Optional[Any]:
    item = _CACHE.get(key)
    if not item:
        return None
    if time.time() - item["ts"] > ttl_seconds:
        _CACHE.pop(key, None)
        return None
    return item["value"]

def set_cached(key: str, value: Any) -> None:
    _CACHE[key] = {"ts": time.time(), "value": value}