#!/usr/bin/env python                                                                                                                                
import sys, os, traceback, numpy, scipy
from optparse import OptionParser
from subprocess import call

n=2000000

numbers=numpy.empty(n/2,dtype=numpy.bool)
numbers[:]=True

for i in xrange(1,n/2):
    for j in xrange(i,(n/2-i)/(2*i+1)+1):
        if i+j+2*i*j<n/2: numbers[i+j+2*i*j]=False

primes=numpy.arange(1,n,2)

primes=primes[numbers]

print primes[10000]
