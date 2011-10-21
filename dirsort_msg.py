#!/usr/bin/env python
# encoding: utf-8
"""
dirsort.py
#   Created on Fri Oct 21 2011 14:21:11 GMT-0400 (EDT) by baisong 
"""

from sys import stdout

def fatal_error(msg):
    prefix = "FATAL:  "
    suffix = "\n"
    stdout.write(prefix + msg + suffix)
    stdout.flush()

def warning(msg):
    prefix = "WARNING:  "
    suffix = "\n"
    stdout.write(prefix + msg + suffix)
    stdout.flush()

def fatal_not_exist(dirname):
    warning('Skipped sorting of %(dirname)s: no such file or directory.' % \
        {"dirname": dirname})
        
def fatal_not_dir(dirname):
    warning('Skipping sorting of %(dirname)s: not a directory.' % \
        {"dirname": dirname})
