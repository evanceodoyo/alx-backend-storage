#!/usr/bin/env python3
"""
Writing strings to redis.
"""
import redis
import uuid
from functools import wraps
from typing import Union, Callable


def count_calls(method: Callable) -> Callable:
    """
    Decorator function that returns a Callable.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator function for recording history of inputs.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(input_key, str(args))
        
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, output)
        return output
    return wrapper


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
    
    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data in Redis using a randomly generated uuid as key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[
            str, int, bytes, float]:
        """"
        Returns value associated with the given key.
        """
        if self._redis.exists(key):
            if fn:
                return fn(self._redis.get(key))
            return self._redis.get(key)
        return None

    def get_str(self, key: str) -> str:
        """
        Retrieve as a str.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Retrieve as int.
        """
        return self.get(key, fn=int)
