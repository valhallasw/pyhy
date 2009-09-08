"""
Creates a 'data.py' file containing all possible responsefields for hyves
"""

import re
import urllib
from BeautifulSoup import BeautifulSoup

version = "1.2.1"
urlroot = "http://trac.hyves-api.nl"

def main():
    soup = BeautifulSoup(urllib.urlopen(urlroot + "/wiki/APIMethods/" + version))
    toc = soup.findAll('div', attrs={'class': 'wiki-toc trac-nav'})[1]
    data = toc.findAll("a", attrs={
                    'href': re.compile(r'/wiki/APIMethods/' + version + '/.+'),
                    'class': 'wiki'})
    parsedata = {}
    for n, link in enumerate(data):
        function = link.string
        print '[%03i%%] %s' % (n*100/len(data), function.encode('utf-8'))
        parsedata[function] = parse_function(link)
    
     open('data.py', 'w').write('aggressive_fields = ' + repr(parsedata) + '\n')

def parse_function(link):
    responsefields = []
    soup = BeautifulSoup(urllib.urlopen(urlroot + link['href']))
    
    try:
        for field in soup.findAll('h4',
            id='methods_'+version+'-'+link.string+'-responsefields') \
            [0].nextSibling.nextSibling.nextSibling.nextSibling:
            responsefields.append(field.next.string)
        return responsefields
    except IndexError:
        return []

if __name__ == '__main__':
    main()
