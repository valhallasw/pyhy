import unittest
import os.path
import codecs

import json
from datetime import datetime

from mock import sentinel

from pyhy.api.registry import HyvesRegistry
from pyhy.api.jsonreader.scrapparser import ScrapParser

class Test(unittest.TestCase):
    def setUp(self):
        self.r = HyvesRegistry(sentinel.connectionobject)
        self.p = ScrapParser(self.r)

    def testParse(self):
        datafile = os.path.join(os.path.split(__file__)[0], 'users.getScraps_homoapi.data')
        scrapjson = json.load(codecs.open(datafile))['scrap'][0]
        scrap = self.p.parse(scrapjson)

        self.assertEqual(scrap, self.r.Scrap(u'cb1040b149d76baa'))
        self.assertEqual(scrap.sender, self.r.User(u'6c7ec0b62fca4e5f'))
        self.assertEqual(scrap.target, self.r.User(u'6f89a2f516034edc'))
        self.assertEqual(scrap.created, datetime(2009, 12, 9, 11, 7, 13))
        self.assertEqual(scrap.body[:10], u'I want my ') 
