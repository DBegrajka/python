fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

#handle = open(name)
#emails = []
counts = dict()
fh = open(fname)
lst = list()
#count = 0
for line in fh:
	if line.startswith('From '):	
		#count = count + 1	
		lst = line.split()
		email = lst[1]		
		counts[email] = counts.get(email,0) + 1		
		#print email
		del lst[:]

#print counts

bigcount = None
bigemail = None
for email,count in counts.items():
	if bigcount is None or count > bigcount:
		bigemail = email
		bigcount = count

print bigemail,bigcount 



#print "There were", count, "lines in the file with From as the first word"

