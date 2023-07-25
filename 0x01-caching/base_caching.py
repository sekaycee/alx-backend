#!/usr/bin/python3
''' base caching module '''


class BaseCaching():
    ''' BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    '''
    MAX_ITEMS = 4

    def __init__(self):
        ''' initialize cache '''
        self.cache_data = {}

    def print_cache(self):
        ''' print the cache '''
        print('Current cache:')
        for key in sorted(self.cache_data.keys()):
            print('{}: {}'.format(key, self.cache_data.get(key)))

    def put(self, key, item):
        ''' add an item in the cache '''
        raise NotImplementedError('put must be implemented in your cache class')

    def get(self, key):
        ''' get an item by key '''
        raise NotImplementedError('get must be implemented in your cache class')
