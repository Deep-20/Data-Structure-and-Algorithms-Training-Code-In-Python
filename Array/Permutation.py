# Given two strings, check if one is permutation of another

list1 = [2,3,5,1,7,9]
list2 = [5,1,9,7,4,2]
flag = 0

if len(list1) == len(list2):
    list1.sort()
    list2.sort()
    if list1 == list2:
        print("Permutation of each other!!")
    else:
        print("Not Permutation")
else:
    print("Not Permutation")

