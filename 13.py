#!/usr/bin/env python                                                                                                                                
import sys, os, traceback, numpy, scipy
from optparse import OptionParser
from subprocess import call



usage="""                                                                                                                                           """

def error(msg):
    os.sys.stderr.write("############# ERROR n#############\n");
    os.sys.stderr.write(msg+"\n")
    os.sys.exit(-1)

# Display a verbose error message & backtrace                                                                                                        
def croak(msg):
    os.sys.stderr.write("############# CROAK #############\n");
    os.sys.stderr.write(msg+"\n")
    traceback.print_stack()
    os.sys.exit(-1)

# Subroutine to safely run a system bash command                                                                                                     
def System(cmd):
    status = call(cmd, shell=True, executable='/bin/bash')
    if status != 0:
      croak("This command failed with return status "+str(status)+": "+cmd)

numbers=numpy.loadtxt("13.dat")

print numpy.sum(numbers)
