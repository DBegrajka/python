import re

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "sum.txt"

y =list()
fh = open(fname)
sum = 0
for line in fh:
	y = re.findall('[0-9]+', line)
#	print y	
	for i in y:	
#		print "hello", i	
		if i is  None: continue	
		x = int(i)
		sum = sum + x
#		print sum
print sum
