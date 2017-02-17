import sys
import random
import os
import time
#Andrew Candelaresi
# 
#HW1 Algorithms
#Selection Sort

	 
	

def main (argv):
	n = int(argv[1])
	a = 10*n
	randomints = []
	elapsed=[]
	
	sum1 = 0
		
	for i in range(0,10):
		randomints = [random.randrange(0,a) for _ in range (n)]
		start =time.clock()
		for k in  range(0, len(randomints)):
			low=k
			for j in range(k, len(randomints)):
				if(randomints[j] <= randomints[low]):
					low=j
			randomints[k], randomints[low] = randomints[low], randomints[k]
			
		elapsed.append(time.clock()-start)
		print randomints
		
	fastest = min(elapsed)
	slowest = max(elapsed)
	averagetime = sum(elapsed)/10
	
		
	print "min = %s" %fastest,  "max = %s" %slowest,  "average = %s" %averagetime
	return
					
				
			
if __name__ == "__main__":
	main(sys.argv)
