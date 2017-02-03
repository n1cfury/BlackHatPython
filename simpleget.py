#!/usr/bin/env python
import urllib2, sys

#TODO: ADD FUNCTIONS

#Simple Get reqeust to a site specified in arguments
host = sys.argv[1]
body = urllib2.urlopen(host)
print body.read()
