#!/usr/bin/env python
import urllib2, sys
#The other example on p 62 using the request class
#TODO: ADD FUNCTIONS
host = sys.argv[1]

headers ={}
headers ['User-Agent'] = "Googlebot"

request = urllib2.Request(host, headers=headers)
response = urllib2.urlopen(request)

print response.read()
response.close()