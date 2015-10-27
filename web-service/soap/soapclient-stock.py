from suds.client import Client
import xml.etree.ElementTree as ET

proxyOpts = dict()
proxyOpts['http'] = 'http://xxx%40xxx:xxx@proxy2.its.ac.id:8080'

url = 'http://www.webservicex.net/stockquote.asmx?WSDL'
client = Client(url, proxy=proxyOpts)

stock = client.service.GetQuote('TLK')
root = ET.fromstring(str(stock))

for child in root:
	for c in child:
		print '%-20s %-30s' % (c.tag, c.text)
