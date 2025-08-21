import numpy as np

#numpy arrays and python lists are two different things --> You cannot perform this operations on python lists
arr1=np.array([1,2,3,4,5])
print(arr1)
print(arr1[1:2])
#2D Arrays in Python Numpy --->
arr2=np.array([[1,2,3,4,5],[6,7,8,9,10]])
#while slicing @d array first argument is dimensiona dnsecond argument is passed as actaual slicing to do that its like an matrix of a mathematics but here the index starts with 0
#For eg : in this arr 2D array )) is the start inde xand can be printted as 
print(arr2[0,0]) #--> output is 1, similrly for pos 1,2 the output will be 8
print(arr2[1,2])
# we can also split he numpy array in this same way
print(arr2[0,2:4])
print(arr2[1,0:2])

# The typecasting can also be done using numpy for eg i can convert the type of array in following ways
#to get data type of array using dtype functions
print(arr1.dtype) #gives int^$ meaning integer data type

#converting the array into float and printing the array with its type
newarr=arr1.astype(float)
#newarr is the copy of the arr1 but in float type
print(newarr.dtype)
print(newarr)

#typecasting in 2D array , converting 2d array ie arr2 into boolean
new2darray=arr2.astype(bool)
print(new2darray.dtype)
print(new2darray)
