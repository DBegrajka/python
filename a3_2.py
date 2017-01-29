# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
add = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
  #  print line
    r = line.find(':')
    data = line[r+1:30]
    #print data
    idata = float(data)
    count = count + 1
    add = add + idata
 #   print idata 		
#print "Done"
avg = add / count 
print "Average spam confidence:", avg 
