class HyvesObject(object):
    """Superclass for all Hyves objects"""
    def __init__(self, obj_id, registry = None):
        self._id = obj_id
        self._registry = registry
