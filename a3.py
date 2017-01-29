# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname,'r')

fr=fh.read()
fk = fr.strip()

print fk.upper()
