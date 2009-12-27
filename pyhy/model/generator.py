from pyhy.model.super import HyvesObject, HyvesProxy, HyvesParser
from pyhy.model.error import HyvesNotLoadedError

class HyvesIterator(object):
    def __init__(self, object_list):
        self._object_list = object_list
        self._loc = -1

    def __iter__(self):
        return self

    def next(self):
        try:
            self._loc += 1
            return self._object_list._items[self._loc]
        except IndexError:
            self._loc -= 1
            if self._object_list._fully_loaded:
                raise StopIteration
            else:
                raise HyvesNotLoadedError("%r has no more %s objects loaded" % (self._object_list._parent, self._object_list._prop))

class HyvesObjectList(HyvesObject):
    """
    >>> obj = HyvesObjectList('parent', 'prop')
    >>> it = obj.__iter__()
    >>> it.next()
    Traceback (most recent call last):
      ...
    HyvesNotLoadedError: 'parent' has no more prop objects loaded
    >>> obj._items.append('item')
    >>> obj._fully_loaded = True
    >>> it.next()
    'item'
    >>> it.next()
    Traceback (most recent call last):
      ...
    StopIteration
    """
    def __init__(self, parent, prop):
        self._parent = parent
        self._prop = prop
        self._items = []
        self._fully_loaded = False

    def __iter__(self):
        return HyvesIterator(self)
