This is an example that shows the connection timeout handling
(in the client).

server.py    -- the server you need to run for this example
client.py    -- client that uses timeout settings


The client disables and enables timeouts to show what happens.
It shows timeouts during long remote method calls, but also timeouts
when trying to connect to a unresponsive server.

Run NS server first using one of these commands:
pyro4-ns 
python -m Pyro4.naming

To check list of remote objects and methods
pyro4-nsc list
