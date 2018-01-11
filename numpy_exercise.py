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