from pyhy.model.super import HyvesObject, HyvesProxy, HyvesParser
from pyhy.model.loadable import Loadable, GLoadable
from pyhy.model.error import HyvesNotLoadedError

class User(HyvesObject):
    """ Defines a User object for hyves.

	Usage:
	>>> u = User('6f89a2f516034edc')
	>>> u.url
        Traceback (most recent call last):
          ...
        HyvesNotLoadedError: url has not been loaded
        
        >>> u.url = u'http://www.google.com'
        >>> u.url
        u'http://www.google.com'
	
        Parameters are available through introspection.
    """

    gloadables = ['friends', 'respects', 'scraps', 'testimonials']
    loadables =  ['about_me', 'birthday', 'city', 'country', 'created',
                  'display_name', 'fancy_layout_tag', 'first_name', 'gender',
                  'locale', 'last_name', 'mobile_url', 'nickname', 'on_my_mind',
                  'profile_picture', 'visible', 'relation_type', 'url',
                  'user_id', 'user_types']

    for item in gloadables:
        locals()[item] = GLoadable(item)
    for item in loadables:
        locals()[item] = Loadable(item)

    def __init__(self, user_id):
        HyvesObject.__init__(self)
        self.user_id = user_id

    def __str__(self):
        try:
            return u'%s (%s %s)' % (self.nickname, self.first_name, self.last_name)
        except HyvesNotLoadedError:
            return u'[u%s]' % (self.user_id,)

    def __repr__(self):
        return "<HyvesUser: %s>" % self.__str__()

class UserParser(HyvesParser):
    @classmethod
    def parse(cls, data):
        obj = User(data['userid'])

        for loadable in obj.loadables:
            setattr(obj, loadable, getattr(cls, 'parse_' + loadable)(data))
    
    for name, jsonname in {'about_me': 'aboutme',
                           'display_name': 'displayname',
                           'fancy_layout_tag': 'fancylayouttag',
                           'first_name': 'firstname',
                           'locale': 'languagelocale',
                           'last_name': 'lastname',
                           'mobile_url': 'mobileurl',
                           'nickname': 'nickname',
                           'on_my_mind': 'onmymind',
                           'url': 'url'}:
        locals()['parse_'+name] = classmethod(lambda c, data: data[jsonname])

    @classmethod
    def parse_birthday(cls, data):
        from datetime import date
        return date(data['birthday']['year'],
                    data['birthday']['month'],
                    data['birthday']['day'])
    
    @classmethod
    def parse_city(cls, data):
        from pyhy.model.city import City
        c = City(data['cityid'])
        if 'cityname' in data:
            c.name = data['cityname']
        return c

    @classmethod
    def parse_country(cls, data):
        from pyhy.model.country import Country
        c = Country(data['countryid'])
        if 'countryname' in data:
            c.name = data['countryname']
        return c
    
    @classmethod
    def parse_created(cls, data):
        from datetime import datetime
        return datetime.fromtimestamp(data['created'])

    @classmethod
    def parse_gender(cls, data):
        from pyhy.enum import Gender
        raise Exception("Not implemented")

    @classmethod
    def parse_profile_picture(cls, data):
        raise Exception("Not implemented")

    @classmethod
    def parse_visible(cls, data):
        raise Exception("Not implemented")

    @classmethod
    def parse_relation_type(cls, data):
        raise Exception("Not implemented")

    @classmethod
    def parse_user_types(cls, data):
        raise Exception("Not implemented")



        obj.birthday = cls.parse_birthday(data)
        obj.city     = cls.parse_city(data)
        obj.country  = cls.parse_country(data)
        obj.created  = cls.parse_timestamp(data['created'])
        obj.on_my_mind = data['onmymind']

        obj.url = data['url']
        obj.mobile_url = data['mobileurl']
        obj.nickname = data['nickname']


        obj.locale = data['languagelocale']
    
        obj.city = cls.parse_city(data)
        obj.country = cls.parse_country(data)

    @classmethod
    def parse_location(cls, data, obj):
        obj.city = City(data['cityid'])
        if 'cityname' in data:
            obj.city.name = data['cityname']
        obj.country = Country(data['countryid'])
        if 'countryname' in data:
            obj.country.name = data['countryname']

    @classmethod
    def parse_enum(cls, data, obj):
        obj.gender = {'male': Gender.Male,
                      'female': Gender.Female}[data['gender']]


