import numpy as np
#trying copy and view functions of array 
arr=np.array([1,2,3,4,5,6,7])
arrcopy=arr.copy()
arrview=arr.view()
arr[0]=9
print(arrview)
# print(arrview) --. prints the changes array but arr.copy just prints the array that was copied initially
print(arrcopy)
#arr.base functions return none if the array owns the data that mean it is copied but returns the original array if it viewed
print(arr.base)    #returns none
print(arrcopy.base) # returns none
print(arrview.base)  #returns arr because it is viewed not copied

