# Andrew Candelaresi
# Algorithms HW 5
import sys
import os



chain = []
twoLetter=[]
threeLetter=[]
fourLetter=[]
fiveLetter=[]
sixLetter=[]
sevenLetter=[]
eightLetter=[]
nineLetter=[]
tenLetter=[]
elevenLetter=[]
twelveLetter=[]
thirteenLetter=[] 
fourteenLetter=[]
fifteenLetter=[]

def containsAll(str, list):
    """Check whether 'str' contains ALL of the chars in 'set'"""
    return 0 not in [c in str for c in list]

def main (argv):
	
	name = argv[1]
	ifile = open(name, "r")
			
	myList = []
	for line in ifile:
		myList.append(line.rstrip())
	
	for i in myList:
		if (len(i) == 2):
			twoLetter.append(i)
		elif(len(i) == 3):
			threeLetter.append(i)
		elif(len(i) == 4):
			fourLetter.append(i)
		elif(len(i) == 5):
			fiveLetter.append(i)
		elif(len(i) == 6):
			sixLetter.append(i)
		elif(len(i) == 7):
			sevenLetter.append(i)
		elif(len(i) == 8):
			eightLetter.append(i)
		elif(len(i) == 9):
			nineLetter.append(i)
		elif(len(i) == 10):
			tenLetter.append(i)
		elif(len(i) == 11):
			elevenLetter.append(i)
		elif(len(i) == 12):
			twelveLetter.append(i)
		elif(len(i) == 13):
			thirteenLetter.append(i)
		elif(len(i) == 14):
			fourteenLetter.append(i)
		elif(len(i) == 15):
			fifteenLetter.append(i)
	
	
	count = 0
	splitletter =[]
	for index in twoLetter:
		for j in threeLetter:
			if 	(containsAll(j, index) != 0):
				chain.extend((index, j))
	print chain
	chain2 = []
	for i in threeLetter:
		for j in fourLetter:
			if 	(containsAll(j, i) != 0):
				for index in range(1,len(chain)-1):
					if (chain[index] == i):
						chain2.extend((i, j))
					index += 2
	print"-----------------------------------------------------\n"
	print"-----------------------------------------------------\n"
	print"-----------------------------------------------------\n"
	print"-----------------------------------------------------\n"
	
		
	#print chain2
	chain3 = []
	for i in fourLetter:
		for j in fiveLetter:
			if 	(containsAll(j, i) != 0):		
				chain3.extend((i, j))
				
	print "\n"
	print "\n"
	print "\n"
	print chain3
	
	chain4 = []
	for i in fiveLetter:
		for j in sixLetter:
			if 	(containsAll(j, i) != 0):		
				chain4.extend((i, j))
				
	
	print "\n"
	print "\n"
	print "\n"
	print chain4
				
	chain5 = []
	for i in sixLetter:
		for j in sevenLetter:
			if 	(containsAll(j, i) != 0):		
				chain5.extend((i, j))
				
	print "\n"
	print "\n"
	print "\n"
	print chain5
	
	chain6 = []
	for i in sevenLetter:
		for j in eightLetter:
			if 	(containsAll(j, i) != 0):		
				chain6.extend((i, j))
				
	print "\n"
	print "\n"
	print "\n"
	print chain6
	
	chain7 = []
	for i in eightLetter:
		for j in nineLetter:
			if 	(containsAll(j, i) != 0):		
				chain7.extend((i, j))
				
	print "\n"
	print "\n"
	print "\n"
	print chain7
	
	chain8 = []
	for i in nineLetter:
		for j in tenLetter:
			if 	(containsAll(j, i) != 0):		
				chain8.extend((i, j))
				
	print "\n"
	print "\n"
	print "\n"
	print chain8
	
	chain9 = []
	for i in tenLetter:
		for j in elevenLetter:
			if 	(containsAll(j, i) != 0):		
				chain9.extend((i, j))
				
	print "\n"
	print "\n"
	print "\n"
	print chain9
	
	chain10 = []
	for i in elevenLetter:
		for j in twelveLetter:
			if 	(containsAll(j, i) != 0):		
				chain10.extend((i, j))
				
	print "\n"
	print "\n"
	print "\n"
	print chain10
	
	
	chain11 = []
	for i in twelveLetter:
		for j in thirteenLetter:
			if 	(containsAll(j, i) != 0):		
				chain11.extend((i, j))
				
	print "\n"
	print "\n"
	print "\n"
	print chain11															
													
	chain12 = []
	for i in thirteenLetter:
		for j in fourteenLetter:
			if 	(containsAll(j, i) != 0):		
				chain12.extend((i, j))
				
	print "\n"
	print "\n"
	print "\n"
	print chain12
	
	chain13 = []
	for i in fourteenLetter:
		for j in fifteenLetter:
			if 	(containsAll(j, i) != 0):		
				chain13.extend((i, j))
				
	print "\n"
	print "\n"
	print "\n"
	print chain13
	 
	
			
				
			
if __name__ == "__main__":
	main(sys.argv)
	
	
	
