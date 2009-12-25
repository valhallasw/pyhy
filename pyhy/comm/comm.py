import logging
import httplib
import oauth.oauth as oauth
from enum import Enum

connectiontype = httplib.HTTPConnection
connectionhost = "data.hyves.nl"
http_method    = "GET"
apiurl = "http://data.hyves-api.nl/"
authurl = "http://www.hyves.nl/api/authorize/"
sgmethod = oauth.OAuthSignatureMethod_HMAC_SHA1()

ExpiryType = Enum('default', 'infinite', 'user')

class HyvesAPIComm(object):
    """ Basic communicator to handle OAuth traffic from and to Hyves.
  
    Usage: c = HyvesAPIClient(consumer_key, consumer_key, ['method', ..])
    i.e. : c = HyvesAPIClient("XXXXXXXXXX", "XXXXXXXXXX", ['users.get'])
  
    Does not check for expiry of request tokens at this moment.
    Does not handle errors at this moment.
    """
    def __init__(self, consumer_key, consumer_secret, methods,
                 expiry=ExpiryType.default, api_version='1.2.1',
                 fancylayout = False, format='json'):
        self.connection = connectiontype(connectionhost)
        self.consumer =  oauth.OAuthConsumer(consumer_key, consumer_secret)
        self.methods = methods if isinstance(methods, list) else [methods]
        self.expiry = expiry
        self.token = None
	self.api_version = api_version
	self.fancylayout = fancylayout
	self.format = format

    def request(self, parameters):
        if not self.token:
            self.get_request_token()
        return self._request(parameters)

    def _request(self, parameters):
        parameters.setdefault('ha_version', self.api_version)
	parameters.setdefault('ha_fancylayout', 'true' if self.fancylayout else 'false')
	parameters.setdefault('ha_format', self.format)
        request = oauth.OAuthRequest.from_consumer_and_token(self.consumer,
                        token=self.token, http_method=http_method,
                        http_url=apiurl, parameters=parameters)
        request.sign_request(sgmethod, self.consumer, self.token)
        logging.debug('%r: request %r' % (self, request.parameters))
        self.connection.request(http_method, request.to_url())
        return self.connection.getresponse().read()

    def get_request_token(self):
        logging.info('%r: acquiring consumer request token' % (self,))
	tdata = self._request(parameters = {'ha_method': 'auth.requesttoken',
                                            'methods': ','.join(self.methods),
                                            'expirationtype': str(self.expiry),
                                            'strict_oauth_spec_response': 'true'})
	self.token = oauth.OAuthToken.from_string(tdata)

    def get_authorize_url(self, callback_url = None):
        if not self.token:
          self.get_request_token()
        if callback_url:
            return oauth.OAuthRequest.from_token_and_callback(
                    token=self.token,
                    http_url=authurl,
                    parameters={'oauth_callback': callback_url}
                   ).to_url()
        else:
            return oauth.OAuthRequest.from_token_and_callback(
                    token=self.token,
                    http_url=authurl
                   ).to_url()

    def authorize(self, verifier):
        logging.info('%r: acquiring user request token' % (self,))
        assert(self.token)
	tdata = self.request(parameters={'ha_method': 'auth.accesstoken',
                                         'strict_oauth_spec_response': 'true'})
	self.token = oauth.OAuthToken.from_string(tdata)
