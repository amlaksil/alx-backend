#!/usr/bin/env python3
"""
This module contains a class called LIFOCache which is a subclass
of BaseCaching that represents a Last-In-First-Out (LIFO) caching system.
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    FIFOCache is a subclass of BaseCaching that represents a
    Last-In-First-Out (LIFO) caching system.

    Attributes:
        queue (list): A list to maintain the order of keys in the LIFO queue.

    """

    def __init__(self):
        """
        Initializes both an instance of LIFOCache by calling the
        constructor of the superclass and an empty queue to maintain
        the order of keys.
        """
        super().__init__()
        self.queue = []  # List to maintain the order of keys

    def put(self, key, item):
        """
        Adds a key-value pair to the cache_data dictionary, following the
        FIFO eviction policy.

        If the cache is already at its maximum capacity (MAX_ITEMS),
        the oldest key-value pair is evicted from the cache based on
        the LIFO order.

        Args:
            key: The key to be added to the cache.
            item: The value associated with the key.

        Returns:
            None
        """
        if key is None or item is None:
            return

        if len(self.queue) >= BaseCaching.MAX_ITEMS:
            if key not in self.queue:
                last_key = self.queue.pop()
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        """
        Retrieves the value associated with the given key from the
        cache_data dictionary.

        Args:
            key: The key to retrieve the value from.

        Returns:
            The value associated with the key if it exists in the cache,
        otherwise None.
        """
        if key is None or key not in self.cache_data.keys():
            return None

        value = self.cache_data[key]
        return value
