import urllib 
from BeautifulSoup import *

import re

#fhand = urllib.urlopen('http://python-data.dr-chuck.net/comments_345786.html' )

url = raw_input('Enter - ')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('span')
sum = 0
for line in tags:
#	print line
	y = line.contents[0]
	x = int(y)
	sum = sum + x
print sum
