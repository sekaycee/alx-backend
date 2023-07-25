#!/usr/bin/env python3
''' first-in first-out caching module. '''
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    ''' represent an object that allows storing and
    retrieving items from a dictionary with a FIFO
    removal mechanism when the limit is reached.
    '''
    def __init__(self):
        ''' initializes the cache. '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        ''' add an item in the cache. '''
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            a_key, _ = self.cache_data.popitem(False)
            print('DISCARD:', a_key)

    def get(self, key):
        ''' retrieve an item by key. '''
        return self.cache_data.get(key, None)
