# Andrew Candelaresi
#collaborators: Peliun Zhang, Austin Holler

import fileinput
import sys


def main (argv):
  filename = argv[2]
  ofile = open(filename, "w")
	
  
  #arrays to hold raw input and size/value results 
  input = []
  dims = []

  #recursive function
  def maxVal(X, Y):
    print "cloth size: ", X, Y
    for i in range(1, X):
      for j in range(1, Y):
        if(maxp[i][j] != -1):
          return maxp[i][j]
        else:
          x=0
          y=0
          for a in range(0, i):
            if(maxp[a][j]+maxp[i-a][j] > a):
              a = maxp[a][j]+maxp[i-a][j]
           

          for b in range(0, j):
            if(maxp[i][j-y]+maxp[i][y] > b):
              b = maxp[i][j-y]+maxp[i][y]			  
          maxp[i][j] = getMax(a, b, price[i][j])
          if (maxp[i][j] > 0):
            print maxp[i][j]
          maxVal(i-1,j-1)
  
  #Read the txt file line by line
  name = argv[1]
  ifile = open(name, "r")
  for line in ifile:
    line = line.split() 
    input.append(line)  

  print "Reading", name
  
  #set values based on first 3 inputs from the file
  X = int(input[0][0])
  Y = int(input[0][1])
  n = int(input[1][0])
  
  #X*Y for price of possible pieces and max prices
  price = [[-1]*Y for _ in range(X)]
  maxp = [[-1]*Y for _ in range(X)] 
  maxp[0][0] = 0


  #fill the dimension array from the input array
  for i in range(2, len(input)-1):
    dims.append(input[i])
  
  #fill prices from the dimension array
  for i in range(0, n-1):
    if(price[int(dims[i][0])][int(dims[i][1])] < int(dims[i][2])):
      price[int(dims[i][0])][int(dims[i][1])] = int(dims[i][2]) 
  
  #call the recursive max value function based on the size of the cloth
  max_val = maxVal(X-1, Y-1)
  
  #write to file
  #with open(filename, "w") as f:
    #f.write(max_val)
	  
  
  
  print "Maximum Return: ", max_val, '\n'

#return the maximum of three values
def getMax(a, b, c):
  if(a > b and a > c):
    print "cut 1"
    return a
  elif(b > a and b > c):
    print "cut 0"
    return b
  else:
    return c 

		
	
	
	
	
				
			
if __name__ == "__main__":
	main(sys.argv)




  
