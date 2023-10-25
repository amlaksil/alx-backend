#!/usr/bin/env python3

"""
This module contains a class called BasicCache which is a
subclass of BaseCaching that represents a basic caching system.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache is a subclass of BaseCaching that represents a basic caching
    system.

    Attributes:
        cache_data (dict): A dictionary to store the key-value pairs as the
        cache.
    """
    def __init__(self):
        """Initializes an instance of BasicCache by calling the superclass's
        constructor.
        """
        super().__init__()

    def put(self, key, item):
        """Adds a key-value pair to the cache_data dictionary.

        Args:
            key: The key to be added to the cache.
            item: The value associated with the key.

        Returns:
            None
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves the value associated with the given key from the
        cache_data dictionary.

        Args:
            key: The key to retrieve the value from.

        Returns:
            The value associated with the key if it exists in the
            cache, otherwise None.
        """
        if key is None or key not in self.cache_data.keys():
            return None
        value = self.cache_data[key]
        return value
