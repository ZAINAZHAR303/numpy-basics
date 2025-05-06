import numpy as np


arr = np.array([8,2,5,1,7])


def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort(arr))


array1 =np.array([1,2,3])
array2 =np.array([4,5,6])
print(np.concatenate((array1,array2),axis=0))
# print(array1.concat(array2))