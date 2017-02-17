#!/usr/bin/python

# Austin Holler
# Algorithms -- HW 7
# Oct 26, 2015
import sys
import numpy

p = numpy.zeros(shape=(50, 20))
P = numpy.zeros(shape=(50, 20))

def maxreturn(i, j):
	if(P[i][j] != -1):
		return P[i][j]
	#if(i == 1 or j == 1):
	#	return p[i][j]
	bestResult = max(p[i][j], maxreturn(i - 1, j) + maxreturn(1, j), maxreturn(i, j-1) + maxreturn(i, 1))
	P[i][j] = bestResult
	return bestResult

#Main function takes command line arguments as n
def main(argv):
	
	data = {}
	
	infile = open(argv[1])
	(len1, len2) = infile.readline().split()
	value_1 = infile.readline().rstrip()
	
	data[int(len1), int(len2)] = int(value_1)
	
	profit = []
	
	for line in infile:
		(x, y, z) = line.split()
		data[int(x), int(y)] = int(z)
		
	for i in range(1, int(len1)):
		for j in range(1, int(len2)):
			p[i][j] = -1
			P[i][j] = -1
			
	for i in xrange(int(len1)):
		for j in xrange(int(len2)):
			if (((i, j) in data) and p[i][j] < data[i, j]):
				p[i][j] = data[i, j]
				
	P[0][0] = 0
	
	print maxreturn(49, 19)
	

#Used for passing command line arguments to main		
if __name__ == "__main__":
	main(sys.argv)
