import rpyc

proxy = rpyc.connect('localhost', 18861, config={'allow_public_attrs': True})
fileobj = open('testfile.txt')
linecount = proxy.root.line_counter(fileobj)
print 'The number of lines in the file was', linecount
