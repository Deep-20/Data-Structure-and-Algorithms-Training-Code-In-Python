from array import *

arr1 = array('i', [1,2,3,4,5,6])

def findElement(array, element):
    for i in range(len(array)):
        if array[i] == element:
            print("Element found in array at position ", i)
            return
    
    else:
        print("Element not found in array!!")
        return

findElement(arr1, 0)