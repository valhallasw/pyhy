import unittest
from pyhy.model.generator import *

class Test(unittest.TestCase):
    def setUp(self):
        self.obj = HyvesObjectList('parent', 'prop')
        self.it  = self.obj.__iter__()

    def test_iterator(self):
        assert(self.it.__iter__() == self.it)

    def test_empty(self):
        self.assertRaises(HyvesNotLoadedError, self.it.next)
        self.assertRaises(StopIteration, self.it.next)

    def test_filled(self):
        self.obj._items.extend([1,2])
        assert(self.it.next() == 1)
        assert(self.it.next() == 2)
        self.assertRaises(HyvesNotLoadedError, self.it.next)
        self.assertRaises(StopIteration, self.it.next)

    def test_fully_loaded(self):
        self.obj._items.append(3)
        self.obj._fully_loaded = True
        assert(self.it.next() == 3)
        try:
            self.it.next()
        except HyvesNotLoadedError:
            raise
        except StopIteration:
            pass
