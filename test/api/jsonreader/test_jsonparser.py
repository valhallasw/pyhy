import unittest
import os.path
import codecs

import json
from datetime import datetime

from mock import sentinel

from pyhy.api.registry import HyvesRegistry
from pyhy.api.jsonreader.jsonreader import JSONReader

class Test(unittest.TestCase):
    def setUp(self):
        self.r = HyvesRegistry(sentinel.connectionobject)
        self.p = JSONReader(self.r)

    def testParse(self):
        datafile = os.path.join(os.path.split(__file__)[0], 'users.getScraps_homoapi.data')
        data = json.load(codecs.open(datafile))
        items = self.p.parse(data)

        self.assert_(self.r.Scrap(u'cb1040b149d76baa') in items)
        self.assert_(self.r.Scrap(u'3c0a2bf0bcb609fc') in items)
