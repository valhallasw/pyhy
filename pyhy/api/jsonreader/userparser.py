class UserParser(object):
    def __init__(self, registry):
        self._registry = registry

    def parse(self, data):
        self.obj = self._registry.User(data['userid'])
        self.parse_strings(data)
        return self.obj

    def parse_strings(self, data):
        for item in ['aboutme', 'displayname', 'fancylayouttag', 'firstname',
                     'languagelocale', 'lastname', 'mobileurl', 'nickname',
                     'onmymind', 'url']:
            vars(self.obj)[item] = data[item]

