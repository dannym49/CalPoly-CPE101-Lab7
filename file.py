# Lab 7 - File I/O
inFile = open("in.txt", "r")
linenum = 0
for line in inFile:
	print("Line %s (%s chars): %s" % (str(linenum), len(line.strip()), line), end='')
	linenum += 1
