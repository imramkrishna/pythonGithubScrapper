import numpy as np
arr1=np.array([1,2,3,4,5,4,5,5,4,4,45,6,4])
#this function where helps to find out the position of certain elements in an array. This function return an array with indexes of element
a=np.where(arr1==4)
#WE CAN ALSO USE IT LIKE A FILTER FUNCTION TO GET A NEW ARRAY WITH CERTAIN CONDITIONS LIKE SHOW BELOW FOR ARRAY b
b=np.where(arr1%2==0)
print(a)
print(b)#this gives the index of array where the condition meets not the actual elements