aggressive_fields = {
	'blogs.create':       ['commentscount', 'respectscount', 'tags', 'geolocation', 'viewscount'],
	'blogs.get':          ['commentscount', 'respectscount', 'tags', 'geolocation', 'viewscount'],
	'blogs.getByGroup':   ['commentscount', 'respectscount', 'tags', 'geolocation', 'viewscount'],
	'blogs.getByHangout': ['commentscount', 'respectscount', 'tags', 'geolocation', 'viewscount'],
	'blogs.getByTag':     ['commentscount', 'respectscount', 'tags', 'geolocation', 'viewscount'],
	'blogs.getByUser':    ['commentscount', 'respectscount', 'tags', 'geolocation', 'viewscount'],
	# ETC
	'users.getByUsername':    ['commentscount', 'respectscount', 'tags', 'fancylayouttag', 'geolocation', 'cityname', 'countryname', 'profilepicture', 'whitespaces', 'onmymind', 'scrapscount', 'testimonialscount', 'respectscount', 'profilevisible', 'scrapsvisible', 'viewscount', 'usertypes', 'relationtype', 'aboutme', 'mobileurl']
	}
# Based on xmlrpclib
# see http://svn.python.org/view/python/trunk/Lib/xmlrpclib.py
class _Method:
    def __init__(self, send, name):
        self.__send = send
        self.__name = name
    def __getattr__(self, name):
        return _Method(self.__send, "%s.%s" % (self.__name, name))
    def __call__(self, **kwargs):
        return self.__send(self.__name, kwargs)

class HyvesAPIProxy:
    def __init__(self, connection, aggressive_loading=False):
        self.conn = connection
	self.aggressive_loading = aggressive_loading

    def __request(self, method_name, params):
	if self.aggressive_loading and method_name in aggressive_fields:
	        params.setdefault('ha_responsefields', aggressive_fields[method_name])

	for key in params:
            if isinstance(params[key], list):
		params[key] = ','.join(params[key])

        params['ha_method'] = method_name
        return self.conn.request(params)

    def __getattr__(self, name):
        return _Method(self.__request, name)
