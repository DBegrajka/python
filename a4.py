fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
#	print line.rstrip()
	for word in line.split():
		if word not in lst:
			lst.append(word)

lst.sort()
print lst[:]
