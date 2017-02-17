
#Andrew candelaresi


import sys
import random
import math
import os
import time

def main (argv):
	n = int(argv[1])
	#to get a random number that has at least n digitss you have to set 
	# the bottom of the range to 10^(n-1) and the top to 10^n
	# I will uses the same logic to generate numbers with n bits
	def make_Prime(n):
		b = 2**(n-5)
		c = (2**(n-4))-1
		prand = random.randint(b,c)
		#I create numbers that are one digit less than the biggest number that I can represent
		#then concatinate them with 3 on the end to increase the chances that I generate a prime
		#also if I find a number that fails my check_primes I add 2 to the previous number and check 
		# again. This way worst case I will be back at 3 in 5 different tries of the check.  Also by adding
		# 2 I will hit 1, 3, 5, 7, which are more likely to be prime numbers.
		p= str(prand) + str(3)
		p= int(p)
		pT = check_primes(p)
		while (pT !=1):
			p=p+2
			pT = check_primes(p)
		return p
		
		
	def check_primes(N):
		for i in range (0,10):
			N
		# here I have implemented Fermat's little theorem
		# by genereating a random int that is less than N 
		# and checking to see if that random int raised to the N-1 mod N is == to 1
		# I run this test 10 times for accuracy in checking.
			a=random.randint(1,N-1)
			if (pow(a, N-1, N) == 1):
				i+=1
			else:
				break
		if (i==10):
			return 1
		else:
			return 0
	start = time.time()			
	p=make_Prime(n)
	q=make_Prime(n)
	time1=(time.time()-start)
	
	N=p*q
	pless=p-1
	qless=q-1
	print "p = %d"  % p, "q = %d" % q
	print "N= %d" % N 
	
	totes = pless * qless
	print "phi(N)= %d" % totes
	def make_e(tot):
		upbound = tot//2
		yrand = random.randint(3,upbound)
		y = str(yrand) +str(3)
		y = int(y)
		yT = check_primes(y)
		while (yT != 1):
			y=y+2
			yT=check_primes(y)
		
		return y
	
	e=make_e(totes)
	print "e = %d" % e
#Use euclid's extended algorithm to find the mulicplicative inverse of 
# e which will be your value for d	
	def ext_Euclid(a,b):
		if (b==0):
			return (1,0,a)
		(x, y, d) =ext_Euclid(b, a%b)
		return (y, x-(a//b)*y, d)
	(x, y, d) = ext_Euclid(e,totes)
	d = x%totes
	print "d= %d" % d
	message = int(2015)
	
	start2=time.time()
	encryption = pow(message, e, N)
	time2 = (time.time()-start2)
	
	print "encry = %d" % encryption
	start3=time.time()
	decryption = pow(int(encryption), int(d), int(N))
	time3 =(time.time()-start3)
	
	print "decry = %d" % decryption
	print "Time: a = %.14f" % time1, "b = %.14f " % time2,"c = %.14f" % time3
	
	return 0
	
	
	
		
		
					
				
			
if __name__ == "__main__":
	main(sys.argv)
