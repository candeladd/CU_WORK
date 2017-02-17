#Andrew Candelaresi
#algorithms homework 3
#finding best subarray
import os
import csv
import sys





def main (argv):
	name = argv[1]
	
	date = []
	Open= []
	ifile = open(name, "rb") 
	stock = csv.reader(ifile)
	rownum = 0
	for row in stock:
		if (rownum == 0):
			head = rownum
			rownum+=1
		else:
			date.append(row[0])
			Open.append(float(row[3]))
	Open.reverse()
	date.reverse()
	print "date range: ", date[0], "-", date[-1]
	ifile.close()
	
	
	#using the guidance in the book I will create a difference array that 
	#tracks the difference in the price of the stock from one day to the next
	size = len(Open)
	diffArr=[]
	for i in range(0, (size-1)):
		diffArr.append(Open[i+1]-Open[i]) 
		i+=1
		
		#using divide and conquer strategy we can start to break the intitial data array into two sub 
		# arrays
		
	fMidd = len(date) - 1
	
	def Find_Max_Cross_sub(A, low, mid, high):
		left_sum = -sys.maxint-1
		sume = 0
		max_left = 0
		max_right = 0
		for i in range (mid, low, -1):
			sume = sume + A[i]
			if (sume >= left_sum):
				left_sum = sume
				max_left = i
		right_sum = -sys.maxint -1
		sume =0
		for j in range (mid+1, high, 1):
			sume = sume+A[j]
			if (sume >= right_sum):
				right_sum = sume
				max_right =j
		return (max_left, max_right, left_sum+right_sum)
		
	
	def Find_Max_sub(A, low, high):
		
		if (high == low):
			return (low, high, A[low])
		else:
			mid = (low+high)//2
			(left_low, left_high, left_sum) = Find_Max_sub(A, low, mid)
			(right_low, right_high, right_sum)= Find_Max_sub(A, mid+1, high)
			(cross_low, cross_high, cross_sum) = Find_Max_Cross_sub(A, low, mid, high)
			if((left_sum >=right_sum) and (right_sum <= cross_sum)):
				return (left_low, left_high, left_sum)
			elif((right_sum >= left_sum) and (right_sum >= cross_sum)):
				return (right_low, right_high, right_sum)
			else:
				return (cross_low, cross_high, cross_sum)
				
	(least, most, MSAsum) = Find_Max_sub(diffArr, 0, len(diffArr)-1)
	print "buy on: ", date[least]
	print "sell on: ", date[most+1]
	print "Maximum Profit: ", MSAsum
	
	
if __name__ == "__main__":
	main(sys.argv)
