import sys
import json

from pyhy.comm import HyvesAPIComm, HyvesAPIProxy
from pyhy.api.registry import HyvesRegistry
from pyhy.api.jsonreader.jsonreader import JSONReader

from config import consumer_key, consumer_pass

if len(sys.argv) != 3:
    print "Syntax: python wall2wall.py username1 username2\n"
    sys.exit()

# oAuth
c = HyvesAPIComm(consumer_key, consumer_pass, 
                 ['users.getByUsername', 'users.getScraps'])
print c.get_authorize_url()
raw_input('Accept and press enter')
c.authorize()
h = HyvesAPIProxy(c, aggressive_loading=True)

jr = JSONReader(HyvesRegistry(None))

(u1, u2) = jr.parse(json.loads(h.users.getByUsername(username=",".join(sys.argv[1:3]))))

s1 = jr.parse(json.loads(h.users.getScraps(target_userid=u1._id)))
s2 = jr.parse(json.loads(h.users.getScraps(target_userid=u2._id)))

scraps = []
scraps.extend(filter(lambda f: f.sender == u2, s1))
scraps.extend(filter(lambda f: f.sender == u1, s2))

scraps.sort(key=lambda f: f.created)

for scrap in scraps:
  print "\n%s\t%s" % (scrap.sender.firstname, scrap.created)
  print "=" * 30
  if len(scrap.body) > 100:
    print scrap.body[:100] + "..."
  else:
    print scrap.body
