import numpy as np
print(np.__version__)
np.show_config()

#create a null vector of size 10
Z = np.zeros(10)
print(Z)

Z[4] = 1
print(Z)

Z = np.arange(10,50)
print(Z)

#reverse a vector
Z = np.arange(50)
Z = Z[::-1] #this is a slice syntax
Z = Z[::2]
print("reverse a vector")
print(Z)

#create a 3*3 matrix with values ranging from 0 to 8
Z = np.arange(9).reshape(3,3)
print(Z)

#find indices of non-zero elements
nz = np.nonzero([0,1,2,3,4,0,0,0])
print(nz)#this method return index

#create a 3*3 identity matrix
Z = np.eye(3)
print(Z)

Z = np.random.random((3,3,3))
print(Z)


#create a 10*10 array with random values and find the minimum and maximum values
Z = np.random.random((10,10))
Zmin, Zmax = Z.min(), Z.max()
print(Zmin, Zmax)

#create a random vector of size 30 and find the mean value
Z = np.random.random(30)
Zmean = Z.mean()
print(Zmean)

#create a 2d array with 1 on the border and 0 inside
Z = np.ones((10,10))
Z[1:-1, 1:-1] = 0 #-1 refers to the last element 
#Z[1,-1] means slicing from the first to the last(not including the last element)
#for example
Z = np.arange(10)
Z = Z[0:1]#slicing the first element
print(Z)

#what is the result of the following expression?

print(np.nan)
print(0 * np.nan) #nan
print(np.nan == np.nan) # false 
print(np.inf > np.nan) # false
print(np.nan - np.nan) # nan
print(0.3 == 3*0.1) # false  0.3 are not representable in binary floating point 

# create a 5*5 matirx with values 1,2,3,4 justr below the diagonal
Z = np.diag(1+np.arange(4), k=-2)#k is offset
print(Z)

Z = np.zeros((8,8), dtype=int)
Z[::2,1::2] = 1 #[start from 0, for every 2 column, start from 1, for every 2 column] 
Z[1::2,::2] = 1
print(Z)


#consider a (6,7,8) shape array, what is the index(x,y,z) of the 100th element
print(np.unravel_index(12,(6,7)))

#create a checkerboard 8*8 matrix using the tile function
Z = np.tile(np.array([[0,1],[1,0]]),(4,4))
print(Z)

#normalize a 5*5 random matrix

Z = np.random.random((5,5))
Zmax, Zmin = Z.max(), Z.min()
Z = (Z-Zmin)/(Zmax-Zmin)
print(Z)
