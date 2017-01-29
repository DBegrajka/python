text = "X-DSPAM-Confidence:    0.8475";
r = text.find('0')
#print text
#print r

data = text[r:30]
#print data
idata = float(data)
print idata
