from array import *


# 1. Create array and traverse it
arr1 = array('i', [1,2,3,4,5,6])

for i in arr1:
    print(i)

# 2. Access individual elements through indices
print("Step 2")
print(arr1[2])
print(arr1[4])

# 3. Append any value to the array using append() method
print("Step 3")
arr1.append(7)
print(arr1)

# 4. Insert value in array using insert() method
print("Step 4")
arr1.insert(0,0)
print(arr1)

# 5. Extend python array using extend() method
print("Step 5")
arr1.extend([8,9,10,11])
print(arr1)

# 6. Add items from list into array using fromlist() method
print("Step 6")
list1 = [12,11,13]
arr1.fromlist(list1)
print(arr1)

# 7. Remove any element using remove() method
print("Step 7")
arr1.remove(0)
print(arr1)

# 8. Remoce last array element using pop() method
print("Step 8")
arr1.pop()
print(arr1)

# 9. Fetch any element from array using index() method
print("Step 9")
print(arr1.index(5))

# 10. Reverse a python array using reverse() method
print("Step 10")
arr1.reverse()
print(arr1)

# 11. Get array buffer information using buffer_info() method
print("Step 11")
print(arr1.buffer_info())

# 12. Check for number of occurences of an element using count() method
print("Step 12")
print(arr1.count(11))

# 13. Convert array to string using tostring() method (Not present in python 3.9 and later)
# print("Step 13")

# 14. Convert array to python list with same elements using tolist() method
print("Step 14")
# print(arr1.tolist())

# 15. Append a string to char arry using fromstring() method (Not present in python 3.9 and later)
# print("Step 15")
# arr2 = array('c', ['h', 'i'])

# 16. Slice elements from an array
print("Step 16")
print(arr1[3:6])
