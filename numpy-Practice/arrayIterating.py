import numpy as np

arr=np.array([2,1,4,2,5,5,2,7])
#This is a traditional way to iterate through an array
print("Elements of 1D array : ",end=" ")
for x in arr:
    print(x,end=" ")
#iterating in a multi dimensional array :
newarray=np.array([[2,3,4],[5,8,6]])
print("\n")
print("Elements of 2D array : ",end=" ")
for x in newarray:
    print("\n")
    for y in x:
        print(y,end=" ")
#for multi-dimensional array :
new3darray=np.array([[[1,2,3],[2,3,4]],[[4,5,6],[7,8,9]]])
print("\n")
print("Elements in 3D array : ",end="")
for x in new3darray:
    for y in x:
        for z in y:
            print(z, end=" ")
print("\n")

#iterating thorugh array using inbuilt algorithms
# 1.using nditer 
print("\nOutput from nditer : ")
arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
#the similar operations can be done without using np.nditer but it will return an array bthis functions directly returns elements
for x in np.nditer(arr2[:,1:2]): 
    print(x)
#this functions gives me index as well as element present there in a multiple dimension array
for index,x in np.ndenumerate(arr2):
    print(index,x)