import rpyc

hello_txt = """
def hello():
    import os
    print "Hello from", os.uname()
"""
con = rpyc.classic.connect("localhost")
print con.modules.os.uname()
print con.modules.sys.version_info
print con.modules.os.getcwd()

con.execute("x = 7")
print con.eval("x + 6")

# print to remote server
con.execute(hello_txt)
remote_hello = con.namespace['hello']
remote_hello()

# redirect to local client
with rpyc.classic.redirected_stdio(con):
    con.namespace['hello']()

rpyc.classic.interact(con)
