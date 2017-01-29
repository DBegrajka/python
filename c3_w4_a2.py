import urllib 
from BeautifulSoup import *

url = raw_input('Enter URL: ')
count1 = raw_input('Enter count: ')
position1 = raw_input('Enter Position: ')

count = int(count1)
position = int(position1)
current_position = 1
current_count = 0
while current_count < count :
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	tags = soup('a')
	print "Retriving..", url 
	for line in tags:
		if position is current_position:
		#	print ' hello', line.contents[0]
			new_url = line.get('href', None)
			#print "Retriving.." new_url
			#print 'Contents:',line.contents[0]
			url = new_url	
			current_position = 1
			break
		current_position = current_position + 1 
	#print current_count
	current_count = current_count + 1
print line.contents[0]
