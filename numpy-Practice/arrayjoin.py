import numpy as np
arr1=np.array([1,2,3,4])
arr2=np.array([6,7,8,9])
arr4=np.array([4,10,11,12])
#this functions concatenates multiple arrays into single array
arr3=np.concatenate((arr1,arr2,arr4))
print(arr3)
#But here is a catch you can only concatenate input arrays with same dimensions
newarr1=np.array([[1,2,3],[4,5,6]])
newarr2=np.array([[2,3,54],[0,7,8],[3,4,5]]) #here matrix order is not same but since dimension is same the arrays gets joined.
newarr=np.concatenate((newarr1,newarr2))
print(newarr)
#you can also join arrays using stack which takes axis as argument and joins in that axis
print("\n")
#but here is a catch in this function as well --> the shape/order of array should be same so this stack fucntion wont join above arrays i will have to create a new one in that same shape as newarr1 inorder to concatenate
newarr3=np.array([[5,7,9],[11,13,15]])
stackarray=np.stack((newarr1,newarr3),axis=2)#this insures that newly generated array joins  the arrays in order as per requirement
print("Array joined by stack : \n",stackarray)
#Stacking along column
columnarray=np.vstack((newarr1,newarr3)) #this means axis=1
print("Stacking along column : \n",columnarray)
#stacking along height
heightarray=np.dstack((newarr1,newarr3)) #this simply means axis=2
print("Stacking along height : \n",heightarray)
