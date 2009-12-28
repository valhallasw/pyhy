import unittest
import os.path

import json

from mock import sentinel

from pyhy.api.registry import HyvesRegistry
from pyhy.api.jsonreader.userparser import UserParser

class Test(unittest.TestCase):
    def setUp(self):
        self.r = HyvesRegistry(sentinel.connectionobject)
        self.p = UserParser(self.r)

    def testParse(self):
        datafile = os.path.join(os.path.split(__file__)[0], 'users.getByUsername_homoapi.data')
        userjson = json.load(open(datafile))['user'][0]
        user = self.p.parse(userjson)

        self.assertEqual(user, self.r.User('6f89a2f516034edc'))
        self.assertEqual(user.url, 'http://homoapi.hyves.nl/')
