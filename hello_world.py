def computepay(h,r):
    k = h-40
    ra = r * 1.5
    if h <= 40 :
    	pay = h *r
	return pay
    else :
    	pay = 40 * r + k * ra
    	return pay
    

hrs = raw_input("Enter Hours:")
ihrs = float(hrs)
rate = raw_input("Enter Rate:")
irate = float(rate)
p = computepay(ihrs,irate)
print "Pay",p



def computepay(h,r):
    k = h-40
    ra = r * 1.5
    
    if h <= 40 :
    	
        pay = h *r
		
        return pay
    
    else :
    	pay = 40 * r + k * ra
    	return pay
    

hrs = raw_input("Enter Hours:")
ihrs = float(hrs)
rate = raw_input("Enter Rate:")
irate = float(rate)
p = computepay(ihrs,irate)
print p
