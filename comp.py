largest = None
smallest = None
a = []
count = 0
while True:

   num = raw_input("Enter a number: ")
     
   if num == "done" : break
   if len(num) < 1 : break
   try:	
   	inum = float(num)
   except:
	print "Invalid Input"
	continue
   a.append(inum)
   count = count + 1 
#    print num

#print "Maximum", largest
for i in range(0, count):
#	print a[i]
	if largest is None :
		largest = a[i]
	elif a[i] > largest :
		largest = a[i]	

print "Maximum", largest

for i in range(0, count):
#	print a[i]
	if smallest is None :
		smallest = a[i]
	elif a[i] < smallest :
		smallest = a[i]	

print "Minimum", smallest





largest = None
smallest = None
a = []
count = 0
while True:

   num = raw_input("Enter a number: ")
     
   if num == "done" : break
   if len(num) < 1 : break
   try:	
   	inum = int(num)
   except:
	print "Invalid input"
	continue
   a.append(inum)
   count = count + 1 
#    print num

#print "Maximum is", largest
for i in range(0, count):
#	print a[i]
	if largest is None :
		largest = a[i]
	elif a[i] > largest :
		largest = a[i]	

print "Maximum is", largest

for i in range(0, count):
#	print a[i]
	if smallest is None :
		smallest = a[i]
	elif a[i] < smallest :
		smallest = a[i]	

print "Minimum is", smallest

