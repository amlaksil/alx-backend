#!/usr/bin/env python3
"""
This module contains a class called MRUCache which is a subclass
of BaseCaching that represents a Most-Recently-Used (MRU) caching system.
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache is a subclass of BaseCaching that represents a
    Most-Recently-Used (MRU) caching system.

    Attributes:
        cache_data (dict): A dictionary to store the key-value pairs
        of the cache.
        queue (list): A list to maintain the order of keys in the LRU queue.

    """

    def __init__(self):
        """
        Initializes both an instance of LRUCache by calling the
        constructor of the superclass and an empty queue to maintain
        the order of keys.
        """
        super().__init__()
        self.queue = []  # List to maintain the order of keys

    def put(self, key, item):
        """
        Adds a key-value pair to the cache_data dictionary, following the
        LRU eviction policy.

        If the cache is already at its maximum capacity (MAX_ITEMS),
        the Most Recently Used (recent key-value pair) is evicted
        from the cache based on the LRU order.

        Args:
            key: The key to be added to the cache.
            item: The value associated with the key.

        Returns:
            None
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key not in self.cache_data.keys():
                oldest_key = self.queue.pop()
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")
            else:
                self.queue.remove(key)

        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        """
        Retrieves the value associated with the given key from the
        cache_data dictionary. Update the access order.

        Args:
            key: The key to retrieve the value from.

        Returns:
            The value associated with the key if it exists in the cache,
        otherwise None.
        """
        if key is None or key not in self.cache_data.keys():
            return None

        self.queue.remove(key)
        self.queue.append(key)

        value = self.cache_data[key]
        return value
