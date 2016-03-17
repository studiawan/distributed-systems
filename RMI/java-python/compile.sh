#!/bin/bash

# java
idlj -fall  Service.idl
javac *.java

# python
omniidl -bpython Service.idl
