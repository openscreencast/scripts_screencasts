#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import urllib2
import simplejson
 
# <ID> wird durch die Youtube-Video-ID ersetzt
handle = urllib2.urlopen("http://gdata.youtube.com/feeds/api/videos/<ID>?v=2&alt=jsonc")
content = handle.read()
j = simplejson.loads(content)
 
print "Titel: {0}".format(j["data"]["title"])
print "Aufrufe: {0}".format(j["data"]["viewCount"])
