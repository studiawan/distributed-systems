import json
import urllib2

# set proxy
proxy_handler = urllib2.ProxyHandler({'https': 'http://xxx%40xxx:xxx@proxy2.its.ac.id:8080'})
opener = urllib2.build_opener(proxy_handler)
urllib2.install_opener(opener)

# request to REST web service
url = 'https://maps.googleapis.com/maps/api/timezone/json?location=-7.2785916,112.7959662&timestamp=1331161200'
response = urllib2.urlopen(url)

# print return value as json
print json.load(response)

