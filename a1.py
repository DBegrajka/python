text = "X-DSPAM-Confidence:    0.8475";
r = text.find(':')
data = text[r+1:30]
    #print data
idata = float(data)
print idata
#fnum = float(num)
#print fnum
