from array import *

arr1 = array('i', [1,2,3,4,5,6])
arr2 = array('d', [1.3, 4.5, 6.7])

print(arr1)
# print(arr2)

# arr1.insert(6,7)

# print(arr1)

# arr2.insert(0,0)
# print(arr2)

def traverseArray(array):
    for i in array:
        print(i)

traverseArray(arr1)