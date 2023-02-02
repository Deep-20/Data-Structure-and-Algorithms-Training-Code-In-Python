# Check if array contains a number in python

from array import *

myArray = array('i', [3,22,45,68,12,90,177,45])
inp = int(input("Enter number to find: "))

if inp in myArray:
    print(inp, " found at index ", myArray.index(inp))
else:
    print("Element not found!")