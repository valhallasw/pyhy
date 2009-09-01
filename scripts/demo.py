import logging
logging.basicConfig(level=logging.DEBUG)
                    #^ set to logging.INFO for less verbose information
from comm import HyvesAPIComm
from hyvesapi import HyvesAPIProxy

# enter private information in seperate file
from config import consumer_key, consumer_pass
# or
#consumer_key = "XXXXXX"
#consumer_pass = "XXXXXX"

c = HyvesAPIComm(consumer_key, consumer_pass, ['users.getByUsername'])
                                             # ^ list of functions to call. Needed to get a token.
print c.get_authorize_url('http://some/url/')
# ^ go there, click accept, copy authorisation string from address and enter at the prompt
c.authorize(raw_input('AUTH >'))

h = HyvesAPIProxy(c)

print h.users.getByUsername(username='homoapi')

