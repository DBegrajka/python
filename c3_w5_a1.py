import urllib
import xml.etree.ElementTree as ET
from BeautifulSoup import *

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

url = raw_input('Enter location: ')
sum = 0
html = urllib.urlopen(url).read()
print "Retriving..", url
print 'Retrieved',len(html),'characters'
#print html
tree = ET.fromstring(html)
lst = tree.findall('comments/comment')
counts = tree.findall('.//count')
print 'Count', len(counts)
for item in lst:
	y = item.find('count').text
	x = int(y)
	sum = sum + x	

print sum

