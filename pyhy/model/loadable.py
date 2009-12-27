from pyhy.model.error import HyvesNotLoadedError
from pyhy.model.generator import HyvesObjectList

class Loadable(object):
    def __init__(self, name):
        self._name = name

    def __get__(self, instance, owner):
        try:
            return instance._storage[self._name]
        except KeyError:
            raise HyvesNotLoadedError("%s has not been loaded" % (self._name))

    def __set__(self, instance, data):
        instance._storage[self._name] = data

class GLoadable(object):
    def __init__(self, name):
        self._name = name

    def __get__(self, instance, owner):
        try:
            return instance._storage[self._name]
        except KeyError:
            instance._storage[self._name] = HyvesObjectList(instance, self._name)

            return instance._storage[self._name]
