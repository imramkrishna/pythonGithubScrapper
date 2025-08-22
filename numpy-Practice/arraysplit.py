import numpy as np
arr1=np.array([[1,2,3],[4,5,6],[8,9,10]])
#array split function helps to split the main array into multiple sub arrays
#this arr_split function not only takes the number of splits but also takes axis like concatente as third argument which is optional
newarr=np.array_split(arr1,6)
#normal split(i.e np.split()) requires equal division but array split which is used above can work with unequal divisions
#array splits --> It splits into n parts as passed by user: If not divisible, the first few get extra elements.
print(newarr)