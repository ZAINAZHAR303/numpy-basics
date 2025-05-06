import numpy as np 

arr = np.arange(10,20)

for i in range (3):
    print(arr[i])
 
print(arr)


# 2nd problem

nums = np.arange(1,11)
print(nums)
even_slice = nums[1:10:2]
print(even_slice)
# change = arr.slice()
even_slice[0]=100
print("original array", nums)
