import urllib2
import simplejson
 
videoid = "52387087"
url = "http://vimeo.com/api/v2/video/" + videoid + ".json"
handle = urllib2.urlopen(url)
content = handle.read()
j = simplejson.loads(content)
 
for key in j[0]:
    print "{0}: {1}".format(key,j[0][key])
