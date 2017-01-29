import urllib 
fhand = urllib.urlopen('http://python-data.dr-chuck.net/comments_42.html' )

for line in fhand:
	print line.strip()

