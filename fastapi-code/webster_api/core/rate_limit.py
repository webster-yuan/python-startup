"""
Simple in-memory rate limiter (dev / single-process).

Enterprise note:
- Production should use a shared store (Redis) to be effective across pods.
"""

from __future__ import annotations

import time
from collections import deque, OrderedDict
from dataclasses import dataclass
from threading import Lock


@dataclass
class _Bucket:
    events: deque[float]
    last_seen: float


class InMemoryRateLimiter:
    """
    In-memory rate limiter with basic DoS protection.

    - max_keys: hard cap on distinct keys to prevent unbounded memory growth
    - idle_ttl_seconds: evict keys that haven't been seen recently (LRU-by-idle)
    """

    def __init__(self, *, max_keys: int = 10_000, idle_ttl_seconds: int = 10 * 60) -> None:
        self._lock = Lock()
        self._max_keys = max_keys
        self._idle_ttl_seconds = idle_ttl_seconds
        # Ordered by last access (LRU); oldest at beginning.
        self._buckets: "OrderedDict[str, _Bucket]" = OrderedDict()

    def _evict_expired_and_overflow(self, now: float) -> None:
        # Evict idle buckets from the LRU head.
        cutoff = now - self._idle_ttl_seconds
        while self._buckets:
            oldest_key, oldest_bucket = next(iter(self._buckets.items()))
            if oldest_bucket.last_seen >= cutoff:
                break
            self._buckets.popitem(last=False)

        # Enforce max keys cap (LRU eviction).
        while len(self._buckets) > self._max_keys:
            self._buckets.popitem(last=False)

    def allow(self, key: str, *, limit: int, window_seconds: int) -> bool:
        now = time.time()
        cutoff = now - window_seconds
        with self._lock:
            self._evict_expired_and_overflow(now)

            bucket = self._buckets.get(key)
            if bucket is None:
                # LRU eviction before inserting a new key
                if len(self._buckets) >= self._max_keys:
                    self._buckets.popitem(last=False)
                bucket = _Bucket(events=deque(), last_seen=now)
                self._buckets[key] = bucket
            else:
                bucket.last_seen = now
                # refresh LRU position
                self._buckets.move_to_end(key, last=True)

            q = bucket.events
            while q and q[0] < cutoff:
                q.popleft()

            if len(q) >= limit:
                return False

            q.append(now)
            # If bucket becomes empty in future requests, it will be evicted by idle TTL.
            return True


rate_limiter = InMemoryRateLimiter()

