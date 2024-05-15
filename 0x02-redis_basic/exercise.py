#!/usr/bin/env python3
"""
Writing strings to redis.
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    Creates a redis instance and stores data.
    """
    def __init__(self):
        """
        Initializes an instance of Redis client as private variable.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data in Redis using a randomly generated uuid as key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
