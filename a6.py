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
		Date = lst[5]
		hr = Date.split(':')	
		fhr = hr[0]		
		counts[fhr] = counts.get(fhr,0) + 1		
		#print email
		del lst[:]

#print counts
for key in sorted(counts):
	print key, counts[key]
#counts.sort()

