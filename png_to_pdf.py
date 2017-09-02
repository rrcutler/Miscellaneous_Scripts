#!/usr/bin/env python
"""
Converts a list of png files to a singular PDF
"""
import sys, os
from fpdf import FPDF

def main( path, inFiles, outfile ):
	pdf = FPDF()

	for image in inFiles:
		pdf.add_page()
		pdf.image(path.replace(' ', '\ ')+image, 1, 1, 200, 200)
	pdf.output(outfile, "F")

def getInput():
	userInput = [] #[[list of .png], outfile
	path = raw_input("Path to folder of .png files\n")
	if (path[-1] != '/'):
		path+='/'
	userInput.append(path)
	userInput.append(next(os.walk(path))[2]) #Appending all files

	userInput.append(raw_input("PDF output\n"))

	return userInput



if __name__ == "__main__":
	userInput = getInput()

	print('List of files being run through:')
	fList=[]
	for files in userInput[1]:
		if ('.png' in files):
			fList.append(files)
			print(files)

	main(userInput[0], fList, userInput[2])