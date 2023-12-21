#!/usr/bin/env python3
""" Main file """
import redis

Cache = __import__('exercise').Cache

cache = Cache()

cache.store(b"first")
print(cache.get(cache.store.__qualname__))

cache.store(b"third")
cache.store(b"second")
print(cache.get(cache.store.__qualname__))
