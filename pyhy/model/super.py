class HyvesObject(object):
    """Superclass of all objects containing Hyves data"""
    def __init__(self):
        self._storage = {}

class HyvesProxy(object):
    """Superclass of all objects retrieving data from the Hyves API

       Tasks:
         * Retrieving unknown data from the API
         * Wrapping objects with the correct wrapper
    """

class HyvesParser(object):
    """Superclass of all parser objects. Parsers parse JSON data into
       pyhy object(s).
    """
