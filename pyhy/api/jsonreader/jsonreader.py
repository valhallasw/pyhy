import json

from userparser import UserParser
from scrapparser import ScrapParser

class JSONReader(object):
    def __init__(self, registry):
        self._registry = registry
        self._parsers = {'user': UserParser,
                         'scrap': ScrapParser
                        }
        for objtype in self._parsers:
            self._parsers[objtype] = self._parsers[objtype](registry = registry)

    def parse(self, data):
        """ Parse a JSON dictionary, as returned by the Hyves API, into objects """
        if data['method'] == 'batch.process':
            return self.parse_batch(data)

        datakeys = [k for k in data.keys() if k not in [u'info', u'method']]

        # We only support single types. Multiple types should only be returned
        # through batch.process, not through any normal function.
        assert(len(datakeys) == 1)

        otype = datakeys[0]
        return [self._parsers[otype].parse(item) for item in data[otype]]
