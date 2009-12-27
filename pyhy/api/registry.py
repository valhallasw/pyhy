from functools import partial

import pyhy.api.model
from pyhy.api.model.object import HyvesObject

def _createGOF(obj):
    def fn(self, obj_id):
        try:
            return self._objects.setdefault(obj, {})[obj_id]
        except KeyError:
            self._objects[obj][obj_id] = obj(obj_id, self)
            return self._objects[obj][obj_id]
    fn.__doc__ = "Return %s object from object pool or create a new object if unavailable" % (obj.__name__,)
    return fn

class HyvesRegistry(object):
    def __init__(self, connection):
        self._connection = connection
        self._objects = {}

    for cls in filter(lambda l: isinstance(l, type) and \
                                issubclass(l, HyvesObject),
                      vars(pyhy.api.model).values()):
        # for every class in pyhy.api.model that is a subclass of HyvesObject
        # N.B. isinstance is needed to prevent TypeErrors from issubclass
        locals()[cls.__name__] = _createGOF(cls)
    del(cls)
