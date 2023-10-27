#!/usr/bin/env python3
"""
This module contains a class called MRUCache which is a subclass
of BaseCaching that represents a Least-Frequently-Used (LFU) caching system.
"""
from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """
    LFUCache is a subclass of BaseCaching that represents a
    Least-Frequently-Used (LFU) caching system.

    Attributes:
        cache_data (dict): A dictionary to store the key-value pairs
        of the cache.
        frequency (defaultdict): A dictionary to store the access
        frequency of each key.
        queue (list): A list to maintain the order of keys in the LRU queue.

    """

    def __init__(self):
        """
        Initializes both an instance of LFUCache by calling the
        constructor of the superclass and an empty queue to maintain
        the order of keys.
        """
        super().__init__()
        self.frequency = defaultdict(int)
        self.queue = []

    def put(self, key, item):
        """
        Adds a key-value pair to the cache_data dictionary, following the
        LRU eviction policy.

        If the cache is already at its maximum capacity (MAX_ITEMS),
        the Least Frequently Used item is evicted from the cache based on
        the LFU order. If there are multiple items with the same least
        frequency, the least recently used item is discarded.

        Args:
            key: The key to be added to the cache.
            item: The value associated with the key.

        Returns:
            None
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update existing key
            self.cache_data[key] = item
            self.frequency[key] += 1
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            min_frequency = min(self.frequency.values())
            least_frequently_used_keys = [k for k, v in self.frequency.items()
                                          if v == min_frequency]
            least_frequently_used_key = least_frequently_used_keys[0]
            del self.cache_data[least_frequently_used_key]
            del self.frequency[least_frequently_used_key]
            self.queue.remove(least_frequently_used_key)
            print("DISCARD:", least_frequently_used_key)

        self.cache_data[key] = item
        self.frequency[key] += 1
        self.queue.append(key)

    def get(self, key):
        """
        Retrieves the value associated with the given key from the
        cache_data dictionary and update the access order.

        Args:
            key: The key to retrieve the value from.

        Returns:
            The value associated with the key if it exists in the cache,
        otherwise None.
        """
        if key is None or key not in self.cache_data.keys():
            return None

        # Update the frequency of the accessed item
        self.frequency[key] += 1
        self.queue.remove(key)
        self.queue.append(key)

        value = self.cache_data[key]
        return value
