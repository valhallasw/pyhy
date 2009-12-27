import unittest
from mock import sentinel

from pyhy.api.registry import HyvesRegistry
from pyhy.api.model import User

class Test(unittest.TestCase):
    def setUp(self):
        self.r = HyvesRegistry(sentinel.connectionobject)

    def test_singleton(self):
        assert id(self.r.User(1)) != id(User(1))
        assert id(self.r.User(1)) == id(self.r.User(1))
        assert self.r.User(1)._id == User(1)._id
        assert id(self.r.User(1)) != id(self.r.User(2))

    def test_connection(self):
        assert self.r.User(1)._registry == self.r
