from datetime import datetime

class ScrapParser(object):
    def __init__(self, registry):
        self._registry = registry

    def parse(self, data):
        self.obj = self._registry.Scrap(data['scrapid'])
        self.obj.sender = self._registry.User(data['userid'])
        self.obj.target = self._registry.User(data['target_userid'])
        self.obj.created = datetime.fromtimestamp(data['created'])
        self.obj.body = data['body']
        return self.obj
