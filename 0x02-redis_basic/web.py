#!/usr/bin/env python3
"""
Request caching and tracking.
"""
import redis
import requests
from functools import wraps
from typing import Callable


r = redis.Redis()


def cacher(fn: Callable) -> Callable:
    """
    A decorator to cache output of fetched data.
    """
    @wraps(fn)
    def wrapper(url: str) -> str:
        """Wrapper function"""
        r.incr(f"count:{url}")
        result = r.get(f"result:{url}")
        if result:
            return result.decode("utf-8")
        result = fn(url)
        r.set(f"count:{url}", 0)
        r.setex(f"result:{url}", 10, result)
        return result
    return wrapper


@cacher
def get_page(url: str) -> str:
    """
    Returns URL contents after caching the request's response and tracking
    the request.
    """
    return requests.get(url).text
