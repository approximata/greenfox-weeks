#!/usr/bin/python

import sys

fuctionlist = ['-l   Lists all the tasks',  '-a   Adds a new task']
pi = sys.argv
print(pi)

def readfunctions(file_name):
    fr = open(file_name)
    text = fr.read()
    fr.close()
    print(text)

readfunctions('todohelp.txt')

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Command line arguments:'
     -l   Lists all the tasks
     -a   Adds a new task
     -r   Removes an task
     -c   Completes an task

str(sys.argv)
