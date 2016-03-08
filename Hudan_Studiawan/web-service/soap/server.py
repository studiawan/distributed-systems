#!/usr/bin/env python

from ladon.ladonizer import ladonize
import math

class Calculator(object):

    @ladonize(float,float,rtype=float)
    def adder(self,a,b):
        return a+b

    @ladonize(float,rtype=float)
    def ceiler(self,a):
        return math.ceil(a)

    @ladonize(float,rtype=float)
    def floorer(self,a):
        return math.floor(a)

    @ladonize(float,float,rtype=float)
    def power(self,a,b):
        return math.pow(a,b)

    @ladonize(float,rtype=float)
    def sqrter(self,a):
        return math.sqrt(a)

    @ladonize(int,rtype=int)
    def factorializer(self,a):
        return math.factorial(a)

    @ladonize(float,rtype=float)
    def sinus(self,a):
        a = math.radians(a)
        return math.sin(a)

    @ladonize(float,rtype=float)
    def cosinus(self,a):
        a = math.radians(a)
        return math.cos(a)

    @ladonize(float,rtype=float)
    def tangent(self,a):
        a = math.radians(a)
        return math.tan(a)


