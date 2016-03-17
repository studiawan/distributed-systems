#!/usr/bin/env python

import sys
from omniORB import CORBA
import CosNaming, _GlobalIDL

# Initialise the ORB
orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)

# Obtain a reference to the root naming context
obj         = orb.resolve_initial_references("PingService")

# Narrow the object to an Example::Echo
eo = obj._narrow(_GlobalIDL.Service)
if eo is None:
    print "Object reference is not an PingService"
    sys.exit(1)

# Call 
message = eo.ping('Hello World!')
print "Java server --> PingService.ping is called ... with", message
