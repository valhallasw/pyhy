import logging
logging.basicConfig(level=logging.DEBUG)
                    #^ set to logging.INFO for less verbose information
from pyhy.comm import HyvesAPIComm, HyvesAPIProxy

# enter private information in seperate file
from config import consumer_key, consumer_pass
# or
#consumer_key = "XXXXXX"
#consumer_pass = "XXXXXX"

import pyhy.comm.data
c = HyvesAPIComm(consumer_key, consumer_pass, 
        pyhy.comm.data.aggressive_fields.keys())
#['users.getByUsername'])
                                             # ^ list of functions to call. Needed to get a token.
print c.get_authorize_url()
# ^ go there, click accept, copy authorisation string from address and enter at the prompt
raw_input('Accept and press enter')
c.authorize()

h = HyvesAPIProxy(c)

print h.users.getByUsername(username='homoapi')

