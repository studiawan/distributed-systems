import rpyc

class MyService(rpyc.Service):
    def exposed_line_counter(self, fileobj):
        linenum = len(fileobj.readlines())
        return linenum

from rpyc.utils.server import ThreadedServer
t = ThreadedServer(MyService, port=18861)
t.start()
