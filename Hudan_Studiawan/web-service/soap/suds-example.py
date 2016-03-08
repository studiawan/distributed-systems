from suds.client import Client

proxyOpts = dict()
proxyOpts['http'] = 'http://proxy_ip_address:8080'

client = Client('http://ladonize.org/python-demos/Calculator/soap/description', proxy=proxyOpts)
 
# Calculate 34+56
result = client.service.add(34,56)
print result
