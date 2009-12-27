import unittest
from pyhy.model.user import *
from pyhy.model.generator import HyvesObjectList

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = u = User('6f89a2f516034edc') #homo api

    def test_loadables(self):
        try:
            self.user.url
        except HyvesNotLoadedError:
            pass
        else:
            fail("unloaded variables should raise HyvesNotLoadedError")

        self.user.url = u"http://www.hyves.nl"
        self.assertEqual(self.user.url, u"http://www.hyves.nl")

    def test_gloadables(self):
        assert(isinstance(self.user.friends, HyvesObjectList))
        self.assertEqual(self.user.friends._parent, self.user)
        self.assertEqual(self.user.friends._prop, "friends")

    def test_str(self):
        self.assertEqual(self.user.__str__(), u'[u6f89a2f516034edc]')
        self.assertEqual(self.user.__repr__(), u'<HyvesUser: [u6f89a2f516034edc]>')
        self.user.nickname = u'Homo API'
        self.user.first_name = u'Homo'
        self.user.last_name = u'Api'
        self.assertEqual(self.user.__str__(), u'Homo API (Homo Api)')
        self.assertEqual(self.user.__repr__(), u'<HyvesUser: Homo API (Homo Api)>')

