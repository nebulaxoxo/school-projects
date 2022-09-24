import numpy as np
# Let first array be first 10 odd numbers:
arr1 = ([1,3,5,7,9,11,13,15,17,19])
# Let second array be first 10 even numbers:
arr2 = ([2,4,6,8,10,12,14,16,18,20])
a = np.add(arr1,arr2)
b = a.tolist() # To separate elements by commas
print("Element-wise sum array is: ", b)

