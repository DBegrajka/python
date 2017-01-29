import urllib
import xml.etree.ElementTree as ET
from BeautifulSoup import *
import json

url = raw_input('Enter location: ')
sum = 0
html = urllib.urlopen(url).read()
print "Retriving..", url
print 'Retrieved',len(html),'characters'
#print html
#tree = ET.fromstring(html)
#lst = tree.findall('comments/count')
info =json.loads(html)
#print info
for item in info["comments"]:
#	print item['count']
	y = item['count']
	x = int(y)
	sum = sum + x	

print sum

