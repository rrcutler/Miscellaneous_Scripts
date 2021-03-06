#!/usr/bin/env python
"""
Gets all the genes that are in the first column of a csv
Skips the header
"""
import sys, csv, os

def main(fName, dirName):
	with open(dirName + fName, 'r') as reader:
		data = [row for row in csv.reader(reader)]


	with open(dirName + fName + '_names.txt', 'w') as writer:
		count = 0
		for row in data:
			if (count != 0):
				writer.write(row[0] + '\n')
			count += 1
	print "Wrote", count, "rows"


def runOnDir(dirName):
	filenames = next(os.walk(dirName))[2]
	for fName in filenames:
		if ('DESeq2') in fName:
			print "Running on file:",  fName
			main(fName, dirName)



if __name__ == "__main__":
	dirName = sys.argv[1]
	if (dirName[-1] != '/'):
		dirName += '/'
	runOnDir(dirName)