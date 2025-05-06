import numpy as np


arr = np.arange(1,10)
# print(np.arrange(15))
print("original array   ", arr)


even_slice = arr[1:10:2] 
print("Even Slice    ", even_slice)


even_slice[0] = 100
print( even_slice)


print("array after modification", arr)
