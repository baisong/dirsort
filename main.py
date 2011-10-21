#!/usr/bin/env python
# encoding: utf-8
"""
dirsort.py
#   Created on Fri Oct 21 2011 14:21:11 GMT-0400 (EDT) by baisong 
"""

import sys, os, stat
import getopt
import dirsort_msg

import dirsort

help_message = '''
The help message goes here.
'''
class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def run(args):
    print 'Welcome to dirsort.py'
    to_be_sorted = []
    for arg in args:
        isdir = False
        try:
            s = os.stat(arg)
            mode = s.st_mode
            isdir = stat.S_ISDIR(mode)
            if isdir:
                to_be_sorted.append(arg)
            else:
                dirsort_msg.fatal_not_dir(arg)
        except:
            dirsort_msg.fatal_not_exist(arg)
            
    for directory in to_be_sorted:
        dirsort.dirsort(directory)
                
    print 'Farewell from dirsort.py'

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "ho:v", ["help", "output="])
        except getopt.error, msg:
            raise Usage(msg)
    
        # option processing
        for option, value in opts:
            if option == "-v":
                verbose = True
            if option in ("-h", "--help"):
                raise Usage(help_message)
            if option in ("-o", "--output"):
                output = value
        
        run(args)
    
    except Usage, err:
        print >> sys.stderr, sys.argv[0].split("/")[-1] + ": " + str(err.msg)
        print >> sys.stderr, "\t for help use --help"
        return 2
if __name__ == "__main__":
    sys.exit(main())
