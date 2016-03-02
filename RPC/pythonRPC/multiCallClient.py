import xmlrpclib

proxy = xmlrpclib.ServerProxy("http://localhost:8000/")
multicall = xmlrpclib.MultiCall(proxy)
multicall.add(2, 3)
multicall.subtract(2, 3)
multicall.multiply(2, 3)
multicall.divide(2.0, 3.0)
result = multicall()

print tuple(result)