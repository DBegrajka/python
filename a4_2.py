fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
lst = list()
count = 0
for line in fh:
	if line.startswith('From '):	
		count = count + 1	
		lst = line.split()
		email = lst[1]
		print email
		del lst[:]
print "There were", count, "lines in the file with From as the first word"

